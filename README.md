# MediaEval2022_Medico

## Demo detection: Yolov5

![](deepsort/yolov5.gif)

## Demo tracking: Yolov5 + DeepSort

![](deepsort/yolov5anddeepsort.gif)

## Installation (Google Colab)

### Task 1 (Detection and Tracking evaluations):

1. Clone this repo and make Task_1 the root directory.

```
git clone https://github.com/LouisDo2108/MediaEval2022_Medico.git
cd /content/MediaEval2022_Medico/Task_1/
```

2. Clone https://github.com/LouisDo2108/ByteTrack.git and setup normally by following the readme.md instructions.

```
cd /content/MediaEval2022_Medico/Task_1/
git clone https://github.com/LouisDo2108/ByteTrack.git
cd ByteTrack
pip3 install -r requirements.txt
python3 setup.py develop
pip3 install cython
pip3 install 'git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI'
pip3 install cython_bbox
```

2. Go back to root folder and clone https://github.com/ultralytics/yolov5 and setup YoloV5 normally by following the readme.md instructions.

```
cd /content/MediaEval2022_Medico/Task_1/
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip3 install -r requirements.txt
```

3. Install the requirements.txt in task_1 folder.

```
cd /content/MediaEval2022_Medico/Task_1/
pip3 install -r requirements.txt
```

4. Download the visem dataset and unzip it to the root folder.

```
cd /content/MediaEval2022_Medico/
unzip {PATH_TO_DATA}/visemtracking.zip -d /content/MediaEval2022_Medico/
```

5. Add ByteTrack folder to Python Path.

```
!export PYTHONPATH="${PYTHONPATH}:{PATH_TO_BYTETRACK}/ByteTrack/"
```

6. Go to Task_1/ and run prepare_data.py. For example:

```
cd /content/MediaEval2022_Medico/Task_1
python /content/MediaEval2022_Medico/Task_1/prepare_data.py \
--root_dir /content/MediaEval2022_Medico/VISEM_Tracking_Train_v4/ \
--gt_dir /content/MediaEval2022_Medico/gt/
```

7. Go to Task_1/ and run Task_1/evaluate.py

```
cd /content/MediaEval2022_Medico/Task_1
python /content/MediaEval2022_Medico/Task_1/evaluate.py \
--result_dir /content/MediaEval2022_Medico/result/ \
--gt_dir /content/MediaEval2022_Medico/gt/ \
--yolo_model_path /content/MediaEval2022_Medico/yolo_trained_models/best.pt
```
