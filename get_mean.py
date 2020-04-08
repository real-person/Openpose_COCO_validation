import os
import cv2
import numpy as np
from get_dataset import imDir


def get_mean(imDir):
    """[summary]
    
    Arguments:
        imDir {[type]} -- [description]
        eqDir {[type]} -- [description]
    """
    img_list = os.listdir(imDir)
    mean_list = [('Image File', 'Mean Intensity')]
    for img_file in img_list:
        # get image path
        img_path = f'{imDir}/{img_file}'
        # Load each image
        img = cv2.imread(img_path)
        # Convert to greyscale
        img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
        # create a CLAHE object (Arguments are optional).
        mean_list.append((img_file, int(np.mean(img_hsv[:, :, 2]))))
    with open('mean.txt', 'w') as f:
        [f.write(f'{m[0]}\t{m[1]}\n') for m in mean_list]


get_mean(imDir)