import helpers
import subprocess
import os
import time

class Processor:
    def __init__(self, video_path):
        self.video_path = video_path

    def process(self, output_folder="output"):
        available_sizes = helpers.get_config("AVAILABLE_SIZES")

        # Create unique directory for each video inside the output folder
        base_name = os.path.splitext(os.path.basename(self.video_path))[0]
        timestamp = int(time.time())
        dir_name = f"{base_name}_{timestamp}"
        dir_path = os.path.join(output_folder, dir_name)
        helpers.make_dir(dir_path)

        outputs = []
        for aspect, sizes in available_sizes.items():
            for size, (width, height, is_landscape, word) in sizes.items():
                # Create subfolder for the word if it doesn't exist
                word_folder = os.path.join(dir_path, word)
                helpers.make_dir(word_folder)

                output_path = os.path.join(
                    word_folder,
                    f"{width}x{height}.mp4"
                )
                vf = f"scale=w={width}:h={height}:force_original_aspect_ratio=decrease,pad={width}:{height}:(ow-iw)/2:(oh-ih)/2"
                command = [
                    helpers.get_path(None, helpers.get_config('PATH_FFMPEG_WINDOWS')),
                    '-i', self.video_path,
                    '-vf', vf,
                    '-c:a', 'copy',
                    output_path
                ]
                subprocess.run(command, check=True)
                outputs.append(output_path)

        return outputs
