#!/bin/bash
#SBATCH -o %j.out
#SBATCH --gres=gpu:1
#SBATCH --nodelist=selab2
#SBATCH --mem-per-cpu=4GB
eval "$(conda shell.bash hook)"
conda activate medico

# Yolov7 detection
CUDA_LAUNCH_BLOCKING=1
python ./yolov7/detect.py \
--img-size 640 \
--source ./data/VISEM-Tracking/VISEM_Tracking_Train_v4/Train/11/11.mp4 \
--weights ./models/yolov7.pt \
--project ../../predictions/ \
--exist-ok --save-txt \
# --suppress