#!/bin/bash
#SBATCH -o %j.out
#SBATCH --gres=gpu:1
#SBATCH --nodelist=selab2
#SBATCH --mem-per-cpu=4GB
eval "$(conda shell.bash hook)"
conda activate medico

CUDA_LAUNCH_BLOCKING=1

# pip install -r requirements.txt
python3 run.py \
    --weights=runs/detect/train7/weights/best.pt \
    --source=datasets/Test/66.mp4 \
    --save-txt \
    --save-json

python3 run.py \
    --weights=runs/detect/train7/weights/best.pt \
    --source=datasets/Test/68.mp4 \
    --save-txt \
    --save-json

python3 run.py \
    --weights=runs/detect/train7/weights/best.pt \
    --source=datasets/Test/73.mp4 \
    --save-txt \
    --save-json

python3 run.py \
    --weights=runs/detect/train7/weights/best.pt \
    --source=datasets/Test/76.mp4 \
    --save-txt \
    --save-json

python3 run.py \
    --weights=runs/detect/train7/weights/best.pt \
    --source=datasets/Test/80.mp4 \
    --save-txt \
    --save-json