from setuptools import find_namespace_packages, setup
import pathlib

with open(
    pathlib.Path(__file__).absolute().parent / "README.md", "r"
) as fh:
    long_description = fh.read()

setup(
    name="rikai-yolov5",
    version="0.1.1",
    license="Apache License, Version 2.0",
    author="Rikai authors",
    author_email="rikai-dev@eto.ai",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tubitv/rikai-yolov5",
    python_requires=">=3.7",
    install_requires=["rikai >= 0.1.8, <=0.1.10", "yolov5 >=6.0.0, <6.1.0", "torch<=1.10.2", "torchvision<=0.11.3"],
    extras_require={
        "dev": [
            "black",
            "isort",
            # for testing
            "pytest",
            "mlflow",
            "rikai-torchhub>=0.1.0",
        ]
    },
    packages=find_namespace_packages(include=["rikai.*"]),
)
