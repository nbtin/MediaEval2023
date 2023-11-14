import argparse

from ultralytics import YOLO

from utils import write_json_file


# https://docs.python.org/3/library/argparse.html
def parse_arguments(parser: argparse.ArgumentParser) -> argparse.Namespace:
    """Parse arguments."""
    parser.add_argument(
        "--task",
        type=str,
        default="detect-track",
        help="'detect' or 'track' or 'detect-track'",
    )
    parser.add_argument(
        "--weights",
        nargs="+",
        type=str,
        default="yolov8n.pt",
        help="model.pt path(s)",
    )
    parser.add_argument(
        "--source",
        type=str,
        default="datasets/Test/66.mp4",
        help="source (file or folder path or webcam number)",
    )
    parser.add_argument(
        "--img-size",
        type=int,
        default=640,
        help="inference size (pixels)",
    )
    parser.add_argument(
        "--project",
        default="../../../predictions",
        help="save results to project/name",
    )
    parser.add_argument(
        "--name",
        default="predict",
        help="save results to project/name",
    )
    parser.add_argument(
        "--save-txt",
        action="store_true",
        help="save results to *.txt",
    )
    parser.add_argument(
        "--exist-ok",
        action="store_true",
        help="existing project/name ok, do not increment",
    )
    parser.add_argument(
        "--save-json",
        action="store_true",
        help="save a cocoapi-compatible JSON results file",
    )
    return parser.parse_args()


def load_model(weights: str) -> YOLO:
    """Load model."""
    return YOLO(weights)


def split_name(name: str) -> str:
    """Split file name.

    Args:
        name: file name
    Returns:
        file name without extension

    For example:
        `datasets/Test/66.mp4` will return 66

    """
    file_name = name.split("/")[-1]
    return file_name.split(".")[0]

def detect(
    model: YOLO,
    source: str,
    img_size: int,
    project: str,
    name: str,
    save_txt: bool = True,
    exist_ok: bool = False,
    save_json: bool = True,
) -> None:
    """Run detecting task."""
    results = model.predict(
        source,
        imgsz=img_size,
        save=True,
        save_txt=save_txt,
        project=project,
        name=name,
        exist_ok=exist_ok,
        save_conf=True,
    )
    if not save_json:
        return
    write_json_file(results[0].tojson(), f"{project}/{name}.json")


def track(
    model: YOLO,
    source: str,
    project: str,
    name: str,
    exist_ok: bool = False,
) -> None:
    """Run tracking task."""
    model.track(
        source,
        project=project,
        name=name,
        exist_ok=exist_ok,
    )


def perform_detect_task(
    model: YOLO,
    name: str,
    opt: argparse.Namespace,
) -> None:
    """Perform detecting task."""
    detect(
        model,
        opt.source,
        opt.img_size,
        opt.project,
        name,
        opt.save_txt,
        opt.exist_ok,
        opt.save_json,
    )


def perform_track_task(
    model: YOLO,
    name: str,
    opt: argparse.Namespace,
) -> None:
    """Perform tracking task."""
    track(
        model,
        opt.source,
        opt.project,
        name,
        opt.exist_ok,
    )


def perform_both_tasks(
    model: YOLO,
    name: str,
    opt: argparse.Namespace,
) -> None:
    """Perform both tasks."""
    perform_detect_task(model, name, opt)
    perform_track_task(model, name, opt)



def main():
    """Main function to detect."""
    parser = argparse.ArgumentParser()
    opt = parse_arguments(parser)
    model = load_model(opt.weights[0])
    name = split_name(opt.source)
    if opt.task == "detect-track":
        perform_both_tasks(model, name, opt)
    elif opt.task == "detect":
        perform_detect_task(model, name, opt)
    elif opt.task == "track":
        perform_track_task(model, name, opt)


if __name__ == "__main__":
    main()
