#  Copyright (c) 2021 Rikai Authors
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from pathlib import Path

import torch
from pyspark.sql import Row, SparkSession
from rikai.types import Image


def test_torchhub(spark: SparkSession):
    work_dir = Path().absolute()
    image_path = f"{work_dir}/tests/assets/test_image.jpg"
    spark.createDataFrame([Row(image=Image(image_path))]).createOrReplaceTempView(
        "images"
    )
    for name in torch.hub.list("ultralytics/yolov5:v6.0"):
        if name.startswith("yolo"):
            sql_text = f"""
                CREATE MODEL {name}
                OPTIONS (device="cpu", batch_size=32)
                USING "torchhub:///ultralytics/yolov5:v6.0/{name}";
            """
            print(sql_text)
            spark.sql(sql_text)
            result = spark.sql(
                f"""
            select ML_PREDICT({name}, image) as pred FROM images
            """
            )

            assert len(result.first().pred) > 0
