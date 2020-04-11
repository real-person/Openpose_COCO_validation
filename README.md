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
    * "System": System type (Windows, Linux or Mac)
    * "Windows Portable Demo": Specifiy whether the windows portable demo is being used (bool)
    * "annType": Type of annotation to use to evaluate against dataset (default: "keypoints")
    * "dataDir": Directory where you want the COCO dtatasets stored (Path/String)
    * "dataType": The type of dataset to downlaod from COCO (default: "val2017")
    * "model_folder": Directory containing the .caffemodel and posedeploy.prototxt files of the model you wish to test (Path/String)
    * "openpose_folder": Path to the directory containing openpose installation (Path/String)
3. Optional - Enable/configure anny of the following entries in the `config` dictionary to take advantage of the image processing functions. Note: If any of the image processing functions are enabled, a seperate "altered" dataset will be created in the same directory as the original.
    * "Equalize": Enables global histogram equalization on the dataset (bool)
    * "Normalize": Enables global contrast stretching on the dataset (bool)
    * "Normalize": Enables global contrast limiting adaptive histogram equalization (CLAHE) on the dataset (bool)
    * "CLAHE clip_limit": Enables global contrast limiting adaptive histogram equalization (CLAHE) on the dataset (bool)
    clip_limit (contrast limit for each grid) parameters to use for CLAHE
    MUST BE "None" AN ITERABLE
    'CLAHE clip_limit': (2.0, 1.0),
    grid_size (side size for each grid) parameters to use for CLAHE
    MUST BE "None" AN ITERABLE
    'CLAHE grid_size': (8, 4, 3, 2),
    Only images with mean intensities below thresh will have CLAHE applied
    MUST BE "None" AN ITERABLE
    'CLAHE threshold': (100, ),
    Set to true to for to perform gamma correction when running get_dataset
    Seperate directory is created for filtered images
    'Gamma': False,
    Gamma values to use for gamma correction
    MUST BE "None" AN ITERABLE
    'Gamma values': [1.5, 2],
    Only images with mean intensities below thresh will be gamma corrected
    MUST BE "None" AN ITERABLE
    'Gamma threshold': (60, 80),
    Set to True to evaluate foot scores instead of body
    NOT CURRENTLY WORKING
    'Foot': False,
    Determines which datasets are validated and evaluated.
    Specify folder names of the datasets
    MUST BE "None" AN ITERABLE
    'Folders to test': ['val2017', ],
    Number of scales to use when running Openpose for validation.
    1 for less memory consumption, 4 for maximum accuracy
    'Scale_number': 1,
    Duration (in seconds) of sleep time between validation runs
    Monitor GPU temp and increase if needed
    'GPU_rest': 5,

