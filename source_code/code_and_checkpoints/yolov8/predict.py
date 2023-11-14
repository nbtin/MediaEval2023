from ultralytics import YOLO
import torch

# check if cuda is available
if torch.cuda.is_available():
    print(torch.cuda.get_device_name())


model = YOLO("runs/detect/train3/weights/best.pt")
# model.predict("datasets/Test/66.mp4", save=True)
model.track("datasets/Test/66.mp4", save=True)
