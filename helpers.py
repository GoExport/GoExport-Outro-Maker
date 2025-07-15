import ctypes
import os
import subprocess
import sys
import config
from modules.logger import logger

def get_config(variable: str, default: str = None):
    return getattr(config, variable, default)

def is_frozen():
    result = getattr(sys, 'frozen', False)
    logger.debug(f"is_frozen() -> {result}")
    return result

def get_cwd():
    """Get the current working directory, using PyInstaller paths if applicable."""
    if is_frozen():
        logger.debug(f"get_cwd() using sys._MEIPASS: {sys._MEIPASS}")
        return sys._MEIPASS
    cwd = os.getcwd()
    logger.debug(f"get_cwd() using os.getcwd(): {cwd}")
    return cwd

def get_path(cwd: str | None = None, *parts):
    """Construct an absolute path, flattening any lists/tuples in parts."""
    if cwd is None:
        cwd = get_cwd()

    # Flatten lists/tuples in parts
    flattened_parts = []
    for part in parts:
        if isinstance(part, (list, tuple)):
            flattened_parts.extend(part)
        else:
            flattened_parts.append(part)

    result = os.path.join(cwd, *flattened_parts)
    logger.debug(f"get_path() cwd={cwd}, parts={flattened_parts} -> {result}")
    return result

def try_command(*input, return_output: bool = False):
    """
    Try to run a command in the shell and return the output or success status.
    If return_output is True, returns the command output as a string.
    :param input: Command and arguments to run.
    :param return_output: If True, returns the command output as a string.
    :return: True if command succeeded, False if it failed, or the output string if return_output is True.
    :raises subprocess.CalledProcessError: If the command fails and check=True is set.
    :raises Exception: For any other unexpected errors.
    """
    try:
        result = subprocess.run(args=input, shell=True, capture_output=True, text=True, check=True)
        logger.debug("Command succeeded: %s", result.stdout)
        return result.stdout.strip() if return_output else True
    except subprocess.CalledProcessError as e:
        logger.error("Error occurred: %s", e)
        logger.error("stderr: %s", e.stderr)  # Optional: Log stderr if needed
        return False
    except Exception as e:
        logger.error("An unexpected error occurred: %s", e)
        return False

def try_path(input):
    result = os.path.exists(input)
    logger.debug(f"try_path() input={input} -> {result}")
    return result

def show_popup(title: str, message: str, type: int = 0):
    if os_is_windows():
        logger.debug(f"show_popup() Windows: title={title}, message={message}, type={type}")
        ctypes.windll.user32.MessageBoxW(None, message, title, type)
    elif os_is_linux():
        logger.debug(f"show_popup() Linux: title={title}, message={message}")
        subprocess.run(["zenity", "--info", "--title", title, "--text", message])
    else:
        logger.debug(f"show_popup() unsupported OS: title={title}, message={message}")
        logger.error("Unsupported OS")

def make_dir(path, reattempt: bool = False):
    original_path = path
    counter = 1
    while True:
        try:
            os.makedirs(path)
            logger.debug(f"Directory created: {path}")
            return True
        except FileExistsError:
            logger.warning(f"Directory {path} already exists.")
            logger.debug(f"make_dir() FileExistsError: path={path}, reattempt={reattempt}")
            if not reattempt:
                return False
            path = f"{original_path}_{counter}"
            counter += 1
        except Exception as e:
            logger.error(f"Failed to create directory {path}: {e}")
            logger.debug(f"make_dir() Exception: {e}")
            return False

# Rest of the helper functions
def os_is_windows():
    result = sys.platform.startswith("win")
    logger.debug(f"os_is_windows() -> {result}")
    return result

def os_is_linux():
    result = sys.platform.startswith("linux")
    logger.debug(f"os_is_linux() -> {result}")
    return result

def os_is_mac():
    result = sys.platform.startswith("darwin")
    logger.debug(f"os_is_mac() -> {result}")
    return result