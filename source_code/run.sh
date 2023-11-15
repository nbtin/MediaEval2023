#!/bin/bash
#SBATCH -o %j.out
#SBATCH --gres=gpu:1
#SBATCH --nodelist=selab2
#SBATCH --mem-per-cpu=4GB
eval "$(conda shell.bash hook)"
conda activate nbtin

CUDA_LAUNCH_BLOCKING=1

cd code_and_checkpoints/yolov8
# pip install -r requirements.txt
python3 run.py \
    --weights=models/yolov8s.pt \
    --source=datasets/Test/66.mp4 \
    --save-txt \
    --save-json \
    --conf=0.25 \
    --iou=0.7 

python3 run.py \
    --weights=models/yolov8s.pt \
    --source=datasets/Test/68.mp4 \
    --save-txt \
    --save-json \
    --conf=0.25 \
    --iou=0.7 

python3 run.py \
    --weights=models/yolov8s.pt \
    --source=datasets/Test/73.mp4 \
    --save-txt \
    --save-json \
    --conf=0.25 \
    --iou=0.7 

python3 run.py \
    --weights=models/yolov8s.pt \
    --source=datasets/Test/76.mp4 \
    --save-txt \
    --save-json \
    --conf=0.25 \
    --iou=0.7 

python3 run.py \
    --weights=models/yolov8s.pt \
    --source=datasets/Test/80.mp4 \
    --save-txt \
    --save-json \
    --conf=0.25 \
    --iou=0.7