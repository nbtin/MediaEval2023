import os
import pathlib

SOURCE_DATA_PATH = "source_code/code_and_checkpoints/data"
DEST_DATA_PATH = "source_code/code_and_checkpoints/yolov8/data"
IMAGES_SUBFOLDER_NAME = "images"
LABELS_SUBFOLDER_NAME = "labels"


def get_all_subdirectories(src_path=SOURCE_DATA_PATH):
    print(src_path)
    return [
        dir
        for dir in os.listdir(src_path)
        if os.path.isdir(os.path.join(src_path, dir))
    ]


def copy_images_and_labels(src_path, dest_path=DEST_DATA_PATH):
    for dir in get_all_subdirectories(src_path):
        images_path = os.path.join(src_path, dir, IMAGES_SUBFOLDER_NAME)
        labels_path = os.path.join(src_path, dir, LABELS_SUBFOLDER_NAME)
        dest_images_path = os.path.join(dest_path, IMAGES_SUBFOLDER_NAME)
        dest_labels_path = os.path.join(dest_path, LABELS_SUBFOLDER_NAME)
        pathlib.Path(dest_images_path).mkdir(parents=True, exist_ok=True)
        pathlib.Path(dest_labels_path).mkdir(parents=True, exist_ok=True)
        print(images_path)
        print(labels_path)
        print(dest_images_path)
        print(dest_labels_path)
        for file in os.listdir(images_path):
            if file.endswith(".jpg"):
                os.system(
                    "cp "
                    + os.path.join(images_path, file)
                    + " "
                    + os.path.join(dest_images_path, file)
                )
                os.system(
                    "cp "
                    + os.path.join(labels_path, file.replace(".jpg", ".txt"))
                    + " "
                    + os.path.join(
                        dest_labels_path,
                        file.replace(".jpg", ".txt"),
                    )
                )


def main():
    copy_images_and_labels(SOURCE_DATA_PATH, DEST_DATA_PATH)
    # handle the case of "23" folder like this
    # cp: source_code/code_and_checkpoints/data/23/labels/23_frame_958.txt:
    # No such file or directory
    # get all images in the folder SOURCE_DATA_PATH/23/images
    # find the corresponding labels in the folder SOURCE_DATA_PATH/23/labels
    # if there are not, delete the image in DEST_DATA_PATH/images
    files = os.listdir(os.path.join(SOURCE_DATA_PATH, "23", "images"))
    for file in files:
        if file.endswith(".jpg"):
            if not os.path.exists(
                os.path.join(
                    SOURCE_DATA_PATH,
                    "23",
                    "labels",
                    file.replace(".jpg", ".txt"),
                ),
            ):
                os.system(
                    "rm "
                    + os.path.join(DEST_DATA_PATH, "images", file)
                )


if __name__ == "__main__":
    main()
