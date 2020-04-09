# Ensure all paths include forward slashs only (No backslash)
# CLAHE and Gamma parameters must be either None or iterables
# Folders to test must be either None or iterables
config = {
    'annType': 'keypoints',
    'dataDir': 'Path/to/where/you/want/dataset',
    'dataType': 'val2017',
    'model_folder': 'path/to/openpose/caffe_model',
    'openpose_folder': 'Path/to/openpose/folder',
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
    'Folders to test': ['val2017', ]
}
