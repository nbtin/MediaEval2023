from ultralytics import YOLO
import torch

# check if cuda is available
print(torch.cuda.is_available())

# load the yolov8 nano model
model = YOLO("yolov8n.pt")

# train the model with the config data input as specified in the data.yaml file
model.train(
    task="detect",
    data="data.yaml",
    epochs=100,
    imgsz=640,
    batch=64,
    plots=True,
)