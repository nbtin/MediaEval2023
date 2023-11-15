from ultralytics import YOLO
import torch

# check if cuda is available
if torch.cuda.is_available():
    print(torch.cuda.get_device_name())


model = YOLO("runs/detect/train7/weights/best.pt")

metrics = model.val(save_json=True, conf=0.25, iou=0.7)
metrics.box.map    # map50-95
metrics.box.map50  # map50
metrics.box.map75  # map75
metrics.box.maps   # a list contains map50-95 of each category