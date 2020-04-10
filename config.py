# Ensure all paths include forward slashs only (No backslash)
# Some parameters must be set to either "None" or iterables (see descriptions)
config = {
    # System type (Linux or Windows)
    'System': 'Windows',
    # Type of annotation to use to evaluate against dataset
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
    'openpose_folder': 'C:/Users/marsh/Desktop/PythonProjects/openpose-1.5.1-binaries-win64-gpu-python-flir-3d_recommended/openpose',
    # Set to true to for global histogram equalization when running get_dataset
    # Seperate directory is created for filtered images
    'Equalize': False,
    # Set to true to for global contrast stretching when running get_dataset
    # Seperate directory is created for filtered images
    'Normalize': False,
    # Set to true to for contrast limiting adaptive histogram equalization
    # (CLAHE) when running get_dataset.
    # Seperate directory is created for filtered images
    'CLAHE': False,
    # clip_limit (contrast limit for each grid) parameters to use for CLAHE
    # MUST BE "None" AN ITERABLE
    'CLAHE clip_limit': (2.0, 1.0),
    # grid_size (side size for each grid) parameters to use for CLAHE
    # MUST BE "None" AN ITERABLE
    'CLAHE grid_size': (8, 4, 3, 2),
    # Only images with mean intensities below thresh will have CLAHE applied
    # MUST BE "None" AN ITERABLE
    'CLAHE threshold': (100, ),
    # Set to true to for to perform gamma correction when running get_dataset
    # Seperate directory is created for filtered images
    'Gamma': False,
    # Gamma values to use for gamma correction
    # MUST BE "None" AN ITERABLE
    'Gamma values': [1.5, 2],
    # Only images with mean intensities below thresh will be gamma corrected
    # MUST BE "None" AN ITERABLE
    'Gamma threshold': (60, 80),
    # Set to True to evaluate foot scores instead of body
    # NOT CURRENTLY WORKING
    'Foot': False,
    # Determines which datasets are validated and evaluated.
    # Specify folder names of the datasets
    # MUST BE "None" AN ITERABLE
    'Folders to test': ['val2017', ],
    # Number of scales to use when running Openpose for validation.
    # 1 for less memory consumption, 4 for maximum accuracy
    'Scale_number': 1,
    # Duration (in seconds) of sleep time between validation runs
    # Monitor GPU temp and increase if needed
    'GPU_rest': 5,
}

# mapping of optimal net resolutions for each model and scale number
net_resolutions = {
    '1_25BSuperModel11FullVGG': {1: "-1x480", 4: "1712x960"},
    '100_135AlmostSameBatchAllGPUs': {1: "-1x480", 4: "1712x960"},
    '1_25BBkg': {1: "-1x368", 4: "1312x736"},
    'body_25b': {1: "-1x368", 4: "1312x736"}
}
