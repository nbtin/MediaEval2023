This project uses the YOLOv8 model to perform object detection and tracking on videos.

# Folder structure
```
.
├── predictions
│   ├── 66
│   │   ├── 66.avi
│   │   ├── 66_detection.json
│   │   ├── 66.mp4
│   │   ├── 66_tracking.mp4
│   │   └── labels
│   │       └── label text files
    ├── ...
├── source_code
│   └── code_and_checkpoints
│   ├── README.md
│       └── yolov8
│           ├── datasets
│           │   ├── Test
│           │   │   ├── 66.mp4
│           │   │   ├── 68.mp4
│           │   │   ├── 73.mp4
│           │   │   ├── 76.mp4
│           │   │   └── 80.mp4
│           │   ├── Train
│           │   │   ├── 13
│           │   │   │   ├── 13.mp4
│           │   │   │   ├── 13.txt
│           │   │   │   ├── images
│           │   │   │   │   └── image frame files (*.jpg)
│           │   │   │   ├── labels
│           │   │   │   │   ├── image frame labels (*.txt)
│           │   │   │   │  
│           │   │   │   ├── labels.cache
│           │   │   │   └── labels_ftid
│           │   │   │       └── labels with feature ID (*.txt)
│           │   │   ├── ...
│           │   └── Val (the same structure as `Train` folder)
│           ├── data.yaml (data configuration file, used for training YOLO model)
│           ├── README.md
│           ├── requirements.txt
│           ├── run.py
│           ├── run.sh
│           ├── train.py
│           ├── ultralytics (YOLOv8 repo folder)
```

# Setup
1. Create a conda environment with `python==3.8`
2. Install dependencies:
```
pip install -r code_and_checkpoints/yolov8/requirements.txt
```

# Run
The shell script is named `run.sh`. This script can be used to run both detection and tracking.
The script takes the following arguments:
- `weights`: the path to the weights file (`*.pt`).
- `source`: the path to the video file (`*.mp4`).
- `task`: the task that you want the model to perform (`detect` or `track` or `detect-track`). Default is `detect-track`, to perform both tasks.
- `img-size`: the input image size of the yolo model. Default is `640`.
- `project`: the path to the output folder. Default is `predictions` folder, "sibling" to the `source_code` folder.
- `name`: the name of the sub-folder of `project`, which contains output for a specific video. The system will automatically get the ID of the video (for example, `66` for `66.mp4`) and use it as the name of the sub-folder.
- `save-txt`: use this flag to save the output in `.txt` format. By default, the `run.sh` will use this flag (recommended).
- `save-json`: use this flag to save detection information in `.json` format. By default, the `run.sh` will use this flag.
- `exist-ok`: use this flag to overwrite the output folder if it already exists. By default, the `run.sh` will not use this flag. For example, if a folder named `66` has already existed, the default command in `run.sh` will create another folder named `662` to store new output.

# Note
If you meet this error (happens when converting from `.avi` file to `.mp4` file)
```
Moviepy - Building video ../../../predictions/662/66.mp4.
Moviepy - Writing video ../../../predictions/662/66.mp4

*** TypeError: must be real number, not NoneType
```
Please upgrade `moviepy` with the below command:
```
pip install --upgrade moviepy
```
