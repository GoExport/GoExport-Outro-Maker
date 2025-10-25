# Configuration
APP_NAME = "GoExport Outro Maker"
APP_VERSION = "1.1.0"
APP_BETA = False
DEFAULT_DEPENDENCIES_FILENAME = "dependencies"
DEFAULT_OUTPUT_FILENAME = "data"

AVAILABLE_ASPECT_RATIOS = [
    "4:3",
    "14:9",
    "9:16",
    "16:9",
]

AVAILABLE_ASPECT_NAMES = {
    "4:3": "standard",
    "14:9": "classic",
    "9:16": "tall",
    "16:9": "wide",
}

AVAILABLE_SIZES = {
    # 4:3
    "4:3": {
        "240p": (320, 240, False, "standard"),
        "360p": (480, 360, False, "standard"),
        "420p": (560, 420, False, "standard"),
        "480p": (640, 480, False, "standard"),
    },

    # 14:9
    "14:9": {
        "360p": (640, 360, False, "classic"),
        "480p": (854, 480, False, "classic"),
        "720p": (1280, 720, False, "classic"),
        "1080p": (1920, 1080, False, "classic"),
        "2k": (2560, 1440, True, 'wide'),
        "4k": (3840, 2160, True, 'wide'),
        "5k": (5120, 2880, True, 'wide'),
        "8k": (7680, 4320, True, 'wide'),
    },

    # 16:9
    "16:9": {
        "360p": (640, 360, True, "wide"),
        "480p": (854, 480, True, "wide"),
        "720p": (1280, 720, True, "wide"),
        "1080p": (1920, 1080, True, "wide"),
        "2k": (2560, 1440, True, 'wide'),
        "4k": (3840, 2160, True, 'wide'),
        "5k": (5120, 2880, True, 'wide'),
        "8k": (7680, 4320, True, 'wide'),
    },

    # 9:16
    "9:16": {
        "360p": (360, 640, False, "tall"),
        "480p": (480, 854, False, "tall"),
        "720p": (720, 1280, False, "tall"),
        "1080p": (1080, 1920, False, "tall"),
    },
}

# Dependencies for Windows
PATH_FFMPEG_WINDOWS = [DEFAULT_DEPENDENCIES_FILENAME, "ffmpeg", "bin", "ffmpeg.exe"]
PATH_FFPROBE_WINDOWS = [DEFAULT_DEPENDENCIES_FILENAME, "ffmpeg", "bin", "ffprobe.exe"]
PATH_FFPLAY_WINDOWS = [DEFAULT_DEPENDENCIES_FILENAME, "ffmpeg", "bin", "ffplay.exe"]

# Development Settings
DEBUG_MODE = False
SKIP_COMPAT = False
FORCE_WINDOW = False