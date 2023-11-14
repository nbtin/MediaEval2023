# Make it work for Python 2+3 and with Unicode
import io
import json

import torch

from ultralytics import YOLO
from ultralytics.engine.results import Results

try:
    to_unicode = unicode
except NameError:
    to_unicode = str

# check if cuda is available
if torch.cuda.is_available():
    print(torch.cuda.get_device_name())


model = YOLO("runs/detect/train3/weights/best.pt")
# model.predict("datasets/Test/66.mp4", save=True)
results = model.predict(
    "datasets/Train/13/images/13_frame_0.jpg",
    save=True,
    save_txt=True,
    project="../../../predictions",
    name="66",
    exist_ok=True,
    save_conf=True,
    save_json=True,
)

print(results)
# Convert results to JSON
print(results[0].tojson())
print(type(results[0].tojson()))
# Save results to JSON
# json.dump(results[0].tojson(), "results.json")
with io.open('data.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(results[0].tojson(),
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=True)
    outfile.write(to_unicode(str_))