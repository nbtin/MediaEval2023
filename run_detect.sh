#!/bin/bash
eval "$(conda shell.bash hook)"
conda activate medico

# Yolov7 detection
CUDA_LAUNCH_BLOCKING=1  
python ./code/yolov7/detect.py \
--img-size 640 \
--source ./videos/66.mp4 \
--weights ./models/yolov7.pt \
--project ./predictions \
--exist-ok --save-txt \
# --suppress