#!/bin/bash
#SBATCH --job-name=nbtin       # create a short name for your job
#SBATCH --nodes=1                # node count
#SBATCH --ntasks=1               # total number of tasks across all nodes
#SBATCH --cpus-per-task=4        # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --mem-per-cpu=4G         # memory per cpu-core (4G is default)
#SBATCH --time=5-00:00:00          # total run time limit (HH:MM:SS)
#SBATCH --mail-type=begin        # send email when job begins
#SBATCH --mail-type=end          # send email when job ends
#SBATCH --mail-user=<YourNetID>@princeton.edu
#Number of GPUs, this can be in the format of "gpu:[1-4]", or "gpu:K80:[1-4] with the type included
#SBATCH --gres=gpu:1
#SBATCH --nodelist=selab2
#SBATCH -oslurm1.out
#SBATCH -eslurm1.err

nvidia-smi
# module purge
# module load anaconda3-2021.05-gcc-9.3.0-r6itwa7
# export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/x86_64-linux-gnu/

# conda init bash
conda activate nbtin
# pip install -r ~/git-repo/MediaEval2023/source_code/code_and_checkpoints/yolov8/requirements.txt

cd source_code/code_and_checkpoints/yolov8
python3 train.py


# conda deactivate
