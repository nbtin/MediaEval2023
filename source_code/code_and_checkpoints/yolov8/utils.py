import io
import json
import moviepy.editor as mp
import torch
import time
from ultralytics import YOLO

try:
    to_unicode = unicode
except NameError:
    to_unicode = str


# https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file
def write_json_file(data, filename):
    with io.open(filename, "w", encoding="utf8") as outfile:
        str_ = json.dumps(
            data,
            indent=4, sort_keys=True,
            separators=(",", ": "),
            ensure_ascii=True,
        )
        outfile.write(to_unicode(str_))



def get_save_dir_from_results(results: list) -> str:
    """Get the saved results directory from YOLO model."""
    return results[0].save_dir


# https://codepal.ai/code-generator/query/Dn3Tabod/convert-avi-to-mp4-python-function
def convert_avi_to_mp4(avi_video_path: str, mp4_dest_video_path: str):
    """
    Converts a movie from AVI format to MP4 format.

    Parameters:
    - input_file: str
        The path or filename of the input AVI file.
    - output_file: str
        The path or filename of the output MP4 file.

    Raises:
    - FileNotFoundError:
        Raises an error if the input AVI file does not exist.
    - OSError:
        Raises an error if there is an issue with the conversion process.

    Returns:
    - None
        The function does not return any value.
        It saves the converted MP4 file to the specified output location.

    """
    try:
        # Load the AVI file
        video = mp.VideoFileClip(avi_video_path)

        # Convert the video to MP4 format
        video.write_videofile(mp4_dest_video_path, codec="libx264")

        print("Conversion completed successfully.")
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Input file '{avi_video_path}' does not exist.",
        )
    except OSError as e:
        raise OSError(f"Error occurred during conversion: {e}")


# https://github.com/LouisDo2108/MediaEval2023-Medico-EvalScript/blob/main/medico_eval_scripts/subtask2_example.py
def print_fps_and_flops(model: YOLO):
    """Print FPS and FLOPS."""
    input_tensor = torch.randn(1, 3, 224, 224)
    # Measure the FPS
    num_runs = 3
    total_time = 0
    for i in range(num_runs):
        start_time = time.perf_counter()
        with torch.no_grad():
            output = model(input_tensor)
        end_time = time.perf_counter()
        total_time += end_time - start_time
    fps = 1 / (total_time / num_runs)

    # Measure the FLOPS
    flops = torch.cuda.memory_allocated() * 2 / (total_time / num_runs)

    print(f"FPS: {fps}")
    print(f"FLOPS: {flops}")
