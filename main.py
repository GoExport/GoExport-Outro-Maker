import helpers
from modules.logger import logger
from modules.processor import Processor
from rich.prompt import Prompt, Confirm, IntPrompt, FloatPrompt

def main():
    # Make the output folder
    helpers.make_dir(helpers.get_path(None, helpers.get_config('DEFAULT_OUTPUT_FILENAME')), False)
    
    # Welcome message
    logger.info(f"Welcome to {helpers.get_config('APP_NAME')} v{helpers.get_config('APP_VERSION')}")

    # Check if FFMPEG exists
    if not helpers.try_path(helpers.get_path(None, helpers.get_config('PATH_FFMPEG_WINDOWS'))):
        logger.error("FFMPEG not found. Please install FFMPEG and try again.")
        return

    while True:
        # Ask the user for the path to the video file
        video_path = Prompt.ask("Please enter the path to your video file")
        if not video_path:
            logger.error("Video path cannot be empty. Please try again.")
            continue

        # Check if the file exists
        if not helpers.try_path(video_path):
            logger.error(f"The file '{video_path}' does not exist. Please check the path and try again.")
            continue

        processor = Processor(video_path)
        output_path = processor.process()

        logger.info(f"Video processed successfully: {output_path}")

if __name__ == '__main__':
    main()