import torch

from ultralytics import YOLO

# check if cuda is available
if torch.cuda.is_available():
    print(torch.cuda.get_device_name())

# load the yolov8 nano model
model = YOLO("yolov8s.pt")

# train the model with the config data input as specified in the data.yaml file
model.train(
    task="detect",
    data="data.yaml",
    epochs=100,
    imgsz=640,
    batch=64,
    plots=True,
)