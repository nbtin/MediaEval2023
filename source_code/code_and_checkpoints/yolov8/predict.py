from ultralytics import YOLO
import torch

# check if cuda is available
if torch.cuda.is_available():
    print(torch.cuda.get_device_name())


model = YOLO("runs/detect/train7/weights/best.pt")
model.predict("datasets/Test/66.mp4", save=True, conf=0.25, iou=0.7, save_json=True)
# model.track("datasets/Test/66.mp4", save=True, conf=0.25, iou=0.7)
