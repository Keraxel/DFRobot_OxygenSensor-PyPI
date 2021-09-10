import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "DFRobot_SEN0322_Oxygen_Sensor",
    version = "1.0.1",
    author = "ZhixinLiu",
    author_email = "zhixin.liu@dfrobot.com",
    description = ("DFRobot SEN0322 Oxygen Sensor library"),
    license = "MIT",
    keywords = "DFRobot Oxygen Sensor",
    url = "https://github.com/Keraxel/DFRobot_OxygenSensor-PyPI",
    packages=['DFRobot_SEN0322_Oxygen_Sensor'],
    install_requires=[
        "smbus"
    ],
    long_description=read('DFRobot_SEN0322_Oxygen_Sensor/README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "License :: OSI Approved :: MIT License",
    ],
)