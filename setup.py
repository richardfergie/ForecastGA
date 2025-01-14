from setuptools import setup, find_packages
import os
import sys

with open("requirements.txt", "r") as f:
    install_requires = f.read().splitlines()

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="forecastga",
    version="0.1.12",
    description="Automated Google Analytics Time Series in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jroakes/forecastga.git",
    author="jroakes",
    author_email="jroakes@gmail.com",
    license="MIT",
    packages=find_packages("src"),
    package_dir={"": "src"},
    requires_python=">=3.6.2",
    install_requires=install_requires,
    include_package_data=True,
    zip_safe=False,
)
