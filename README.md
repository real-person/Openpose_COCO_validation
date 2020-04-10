# Openpose_COCO_validation
This repo levages the python COCO API and adapts parts of the Openpose traing/validation code help automate the validation of any openpose models on any COCO dataset. In addition, functions are included for preprocessing the COCO datasets with several low level image processing techniques to test their effects on model accuracy.

## Prerequesits
Package requirements are listed in [requirements.txt](requirements.txt). On Windows, to pip install pycocotools (using requirements.txt), you must have the Visual C++ 2015 build tools installed. You can download them [here](https://go.microsoft.com/fwlink/?LinkId=691126).

A functioning Openpose build is required to run the validation of the models. They can be obtained directly from the [releases section](https://github.com/CMU-Perceptual-Computing-Lab/openpose/releases) of the Openpose repo (Windows Portable Demo). If you are on a Linux/Mac machione, or you wish to customize your Openpose build you must build it from the source code. For instructions on how to do this, refer to the [installation document](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/installation.md) on the Openpose repo.

### Optional
This repo includes the functionality for testing Openpose's improved experimental models from the [Single-Network Whole-Body Pose Estimation](https://arxiv.org/abs/1909.13423) paper. Download links, and instructions on how to add the models to Openpose can be found at the [experimantal models](https://github.com/CMU-Perceptual-Computing-Lab/openpose_train/tree/master/experimental_models) section of the [openpose_train](https://github.com/CMU-Perceptual-Computing-Lab/openpose_train) repository.

## Installation
Ensure that you have all of the required prerequisites before proceding with installation.
1. Clone the repository and run `pip install -r requirements.txt`
2. Enter the following information into the `config` dictionary in config.py
    * 'System': System type (Windows, Linux or Mac)
    * 'Windows Portable Demo': Specifiy whether the windows portable demo is being used (True/False)
    * 'annType': Type of annotation to use to evaluate against dataset
    'annType': 'keypoints',
    # Directory where the user wishes to store COCO dtatasets
    'dataDir': 'C:/Users/marsh/Pictures/COCO',
    # The type of dataset to downlaod from COCO
    'dataType': 'val2017',
    # Path to the directory containing the .caffemodel and posedeploy.prototxt
    # files of the model you wish to test
    'model_folder': 'C:/Users/marsh/Documents/GitHub/openpose_train/experimental_models/1_25BSuperModel11FullVGG/body_25b',
    # Path to the directory containing openpose binaries
    # Inside this directory there should be a "bin" directory containing OpenPoseDemo.exe


