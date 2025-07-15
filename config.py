# Configuration
APP_NAME = "GoExport Outro Maker"
APP_VERSION = "1.0.0"
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
        "320x240": (320, 240, False, "standard"),
        "480x360": (480, 360, False, "standard"),
        "560x420": (560, 420, False, "standard"),
        "640x480": (640, 480, False, "standard"),
    },

    # 14:9
    "14:9": {
        "640x432": (640, 432, False, "classic"),
        "720x480": (720, 480, False, "classic"),
        "768x576": (768, 576, False, "classic"),
        "848x576": (848, 576, False, "classic"),
    },

    # 16:9
    "16:9": {
        "640x360": (640, 360, True, "wide"),
        "854x480": (854, 480, True, "wide"),
        "1280x720": (1280, 720, True, "wide"),
        "1920x1080": (1920, 1080, True, "wide"),
    },

    # 9:16
    "9:16": {
        "360x640": (360, 640, False, "tall"),
        "480x854": (480, 854, False, "tall"),
        "720x1280": (720, 1280, False, "tall"),
        "1080x1920": (1080, 1920, False, "tall"),
    },
}

# Dependencies for Windows
PATH_FFMPEG_WINDOWS = [DEFAULT_DEPENDENCIES_FILENAME, "ffmpeg", "bin", "ffmpeg.exe"]
PATH_FFPROBE_WINDOWS = [DEFAULT_DEPENDENCIES_FILENAME, "ffmpeg", "bin", "ffprobe.exe"]
PATH_FFPLAY_WINDOWS = [DEFAULT_DEPENDENCIES_FILENAME, "ffmpeg", "bin", "ffplay.exe"]

# Development Settings
DEBUG_MODE = False
SKIP_COMPAT = False
