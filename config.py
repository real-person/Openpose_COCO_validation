# Ensure all paths include forward slashs only (No backslash)
# CLAHE and Gamma parameters must be either None or iterables
# Folders to test must be either None or iterables
config = {
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
    'Equalize': False,
    'Normalize': False,
    'CLAHE': False,
    'CLAHE clip_limit': (2.0, 1.0),
    'CLAHE grid_size': (8, 4, 3, 2),
    'CLAHE threshold': (100, ),
    'Gamma': False,
    'Gamma values': [1.5, 2],
    'Gamma threshold': (60, 80),
    'Foot': False,
    'Folders to test': ['val2017', ],
    # 1 for less memory consumption, 4 for maximum accuracy
    'Scale_number': 1,
    # Duration (in seconds) of sleep time between validations runs
    'GPU_rest': 5,
}

net_resolutions = {
    '1_25BSuperModel11FullVGG': {1: "-1x480", 4: "1712x960"},
    '100_135AlmostSameBatchAllGPUs': {1: "-1x480", 4: "1712x960"},
    '1_25BBkg': {1: "-1x368", 4: "1312x736"},
    'body_25b': {1: "-1x368", 4: "1312x736"}
}
