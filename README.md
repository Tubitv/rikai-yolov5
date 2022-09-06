# Yolov5 support for Rikai
```
./pants run src/python/yolov5/detect.py -- --source tests/assets/test_image.jpg
```

# Yolov5 support for Rikai
`rikai-yolov5` integrates Yolov5 implemented in PyTorch with Rikai. It is based
on the [packaged ultralytics/yolov5](https://github.com/fcakyon/yolov5-pip).

## Notebooks
+ <a href="https://colab.research.google.com/github/eto-ai/rikai/blob/main/notebooks/Mojito.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> Using Rikai to analyze an image from Jay Chou's Mojito.

## Usage
There are two ways to use `rikai-yolov5`.

``` python
rikai.mlflow.pytorch.log_model(
    model,
    "model",
    OUTPUT_SCHEMA,
    registered_model_name=registered_model_name,
    model_type="yolov5",
)
```

Another way is setting the model_type in Rikai SQL:
```
CREATE MODEL mlflow_yolov5_m
MODEL_TYPE yolov5
OPTIONS (
  device='cpu'
)
USING 'mlflow:///{registered_model_name}';
```

## Available Options

| Name | Default Value | Description |
|------|---------------|-------------|
| conf_thres | 0.25 | NMS confidence threshold |
| iou_thres  | 0.45 | NMS IoU threshold |
| max_det    | 1000 | maximum number of detections per image |
| image_size | 640  | Image width |

Here is a sample usage of the above options:

``` sql
CREATE MODEL mlflow_yolov5_m
OPTIONS (
  device='cpu',
  iou_thres=0.5
)
USING 'mlflow:///{registered_model_name}';
```
