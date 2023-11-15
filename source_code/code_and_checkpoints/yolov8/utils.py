import io
import json
import moviepy.editor as mp

try:
    to_unicode = unicode
except NameError:
    to_unicode = str


def create_json_data(raw_data):
    """
    Create JSON data from raw data.
    """
    results = []
    for i in range(len(raw_data)):
        data = raw_data[i]
        for j in range(len(data.boxes.xyxy)):
            json_data = {
                "bbox": [round(num, 5) for num in data.boxes.xyxy[j].tolist()],
                "category_id": int(data.boxes.cls[j]),
                "image_id": i + 1,
                "score": round(float(data.boxes.conf[j]), 5),
            }
            results.append(json_data)
    return results

# https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file
def write_json_file(data, filename):
    json_data = create_json_data(data)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)



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
