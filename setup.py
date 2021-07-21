#!/usr/bin/env python
from setuptools import setup, find_packages
setup(
    name="FastSurfer",
    packages=find_packages(include=['FastSurferCNN', 'FastSurferCNN.models','FastSurferCNN.data_loader']),
    install_requires=[
        "cycler>=0.10.0",
        "decorator>=4.4.2",
        "h5py>=2.9.0",
        "imageio>=2.9.0",
        "kiwisolver>=1.2.0",
        "matplotlib>=3.1.1",
        "networkx>=2.5",
        "nibabel>=2.5.1",
        "numpy>=1.17.4",
        "Pillow>=8.2.0",
        "pyparsing>=2.4.7",
        "python-dateutil>=2.8.1",
        "PyWavelets>=1.1.1",
        "scikit-image>=0.15.0",
        "scipy>=1.3.1",
        "six>=1.15.0",
    ],
    python_requires=">=3.6",
)
