# Openpose_COCO_validation
This repo leverages the python COCO API and adapts parts of the Openpose traing/validation code help automate the validation of openpose models on COCO datasets. In addition, functions are included for preprocessing the COCO datasets with several low level image processing techniques to test their effects on model accuracy.

## Prerequesits
Package requirements are listed in [requirements.txt](requirements.txt). On Windows, to pip install [pycocotools](https://github.com/philferriere/cocoapi/tree/master/PythonAPI/pycocotools) (using requirements.txt), you must have the Visual C++ 2015 build tools installed. You can download them [here](https://go.microsoft.com/fwlink/?LinkId=691126).

A functioning Openpose build is required to run the validation of the models. They can be obtained directly from the [releases section](https://github.com/CMU-Perceptual-Computing-Lab/openpose/releases) of the Openpose repo (Windows Portable Demo). If you are on a Linux/Mac machione, or you wish to customize your Openpose build you must build it from the source code. For instructions on how to do this, refer to the [installation document](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/installation.md) on the Openpose repo.

### Optional
This repo includes the functionality for testing Openpose's improved experimental models from the [Single-Network Whole-Body Pose Estimation](https://arxiv.org/abs/1909.13423) paper. Download links, and instructions on how to add the models to Openpose can be found at the [experimantal models](https://github.com/CMU-Perceptual-Computing-Lab/openpose_train/tree/master/experimental_models) section of the [openpose_train](https://github.com/CMU-Perceptual-Computing-Lab/openpose_train) repository.

## Installation
Ensure that you have all of the required prerequisites before proceding with installation.
1. Clone the repository and run `pip install -r requirements.txt`
2. Enter the following information into the `config` dictionary in config.py
    * "System": System type ("Windows", "Linux", or "Mac")
    * "Windows Portable Demo": Specifiy whether the windows portable demo is being used (bool)
    * "annType": Type of annotation to use to evaluate against dataset (string, default: "keypoints")
    * "dataDir": Directory where you want the COCO dtatasets stored (path/string)
    * "dataType": The type of dataset to downlaod from COCO (string, default: "val2017")
    * "model_folder": Directory containing the .caffemodel and posedeploy.prototxt files of the model you wish to test (path/string)
    * "openpose_folder": Path to the directory containing openpose installation (Path/String)
3. Optional - Enable/configure anny of the following entries in the `config` dictionary to take advantage of the image processing functions. Note: If any of the image processing functions are enabled, a seperate "altered" dataset will be created in the same directory as the original.
    * "Equalize": Enables global histogram equalization on the dataset (bool)
    * "Normalize": Enables global contrast stretching on the dataset (bool)
    * "Normalize": Enables global contrast limiting adaptive histogram equalization (CLAHE) on the dataset (bool)
    * "CLAHE": Enables global contrast limiting adaptive histogram equalization (CLAHE) on the dataset (bool)
    * "CLAHE clip_limit": Parameter for CLAHE function specifying the maximum contrast limit for each grid (Iterable of floats or "None")
    * "CLAHE grid_size": Parameter for CLAHE function specifying the side length of each grid (Iterable of floats or "None")
    * "CLAHE threshold": Only images with mean intensities below the threshold will have CLAHE applied (Iterable of floats or "None")
    * "Gamma": Enables gamma correction on the dataset (bool)
    * "Gamma values": Gamma values to use for gamma correction (Iterable of floats or "None")
    * "Gamma threshold": Only images with mean intensities below thresh will be gamma corrected (Iterable of floats or "None")
    * "Folders to test": Names of the folders containing the datasets that you want to validate and evaluate. (Iterable of strings or "None")
    * "Scale_number": Number of scales to use when running Openpose for validation(1 for less memory consumption, 4 for maximum accuracy). (int)
    * "GPU_rest": Duration (in seconds) of sleep time between validation runs. Monitor GPU temp and increase if needed (int)

## Operation
Once config.py is complete with the necessary data, simply run "run.py". This downloads, filters, validates with openpose and prints a summary of the results for each run. 