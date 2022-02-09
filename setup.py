from setuptools import find_namespace_packages, setup
import pathlib

with open(
    pathlib.Path(__file__).absolute().parent / "README.md", "r"
) as fh:
    long_description = fh.read()

setup(
    name="rikai-yolov5",
    version="0.0.5",
    license="Apache License, Version 2.0",
    author="Rikai authors",
    author_email="rikai-dev@eto.ai",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tubitv/rikai-yolov5",
    python_requires=">=3.7",
    install_requires=["rikai >= 0.1.2", "yolov5 >=6.0.0, <7.0.0"],
    extras_require={
        "dev": [
            "black",
            "isort",
            # for testing
            "pytest",
            "mlflow",
            "rikai-torchhub"
        ]
    },
    packages=find_namespace_packages(include=["rikai.*"]),
)
