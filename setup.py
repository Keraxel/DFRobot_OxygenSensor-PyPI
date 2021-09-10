import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "python-dfrobot-sen0322-oxygen-sensor",
    version = "1.0.0",
    author = "ZhixinLiu",
    author_email = "zhixin.liu@dfrobot.com",
    description = ("DFRobot Oxygen Sensor library"),
    license = "MIT",
    keywords = "DFRobot Oxygen Sensor",
    url = "https://github.com/Keraxel/DFRobot_OxygenSensor-PyPI",
    packages=['python-dfrobot-sen0322-oxygen-sensor'],
    long_description=read('python-dfrobot-sen0322-oxygen-sensor/README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "License :: OSI Approved :: MIT License",
    ],
)