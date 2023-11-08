# https://www.freecodecamp.org/news/how-to-detect-objects-in-images-using-yolov8/#get_started
from ultralytics import YOLO

model = YOLO("../models/yolov8m.pt")

results = model.predict(
    source="../data/VISEM-Tracking/VISEM_Tracking_Train_v4/Train/12/12.mp4",

)

# result = results[0]
# print(len(result.boxes))
