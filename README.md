# Openpose_COCO_validation
This repo levages the python COCO API and adapts parts of the Openpose traing/validation code help automate the validation of any openpose models on any COCO dataset. In addition, functions are included for preprocessing the COCO datasets with several low level image processing techniques to test their effects on model accuracy.

## Prerequesits
Package requirements are listed in [requirements.txt](requirements.txt). On Windows, to pip install pycocotools (using requirements.txt), you must have the Visual C++ 2015 build tools installed. You can download them [here](https://go.microsoft.com/fwlink/?LinkId=691126).

The Openpose binaries required to run the validation of the models. They can be obtained directly from the [releases section](https://github.com/CMU-Perceptual-Computing-Lab/openpose/releases) of the Openpose repo (Windows only), or you can build them yourself. For instructions on building Openpose from the source code, refer to the [installation document](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/installation.md) on the Openpose repo.

This repo includes the functionality for testing the CMU's experimental models from the [Single-Network Whole-Body Pose Estimation](https://arxiv.org/abs/1909.13423) paper. Download links, and instructions on how to add the models to Openpose can be found at the [experimantal models](https://github.com/CMU-Perceptual-Computing-Lab/openpose_train/tree/master/experimental_models) section of the [openpose_train](https://github.com/CMU-Perceptual-Computing-Lab/openpose_train) repo.


