import os
import cv2
import numpy as np


def normalize_dataset(imDir, normDir):
    """Performs normalized (0 - 1.0) contrast stretching on a given dataset

    Arguments:
        imDir {String} -- Path to the directory containing the image dataset
        normDir {String} -- Path of directory to save the filtered dataset
    """
    img_list = os.listdir(imDir)
    num_imgs = len(img_list)
    i = 1
    for img_file in img_list:
        if i % (num_imgs/5) == 0 or i == 1:
            print(f'Processing image {i}/{num_imgs}')
        # get image path
        img_path = f'{imDir}/{img_file}'
        # Create path for equalized image
        img_eq_path = f'{normDir}/{img_file}'
        # Load each image
        img = cv2.imread(img_path)
        # normalize float versions
        norm_img = cv2.normalize(img, None, alpha=0, beta=1,
                                 norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
        # scale to uint8
        norm_img = (255 * norm_img).astype(np.uint8)
        # Save normalized image to normDir using the same filename
        cv2.imwrite(img_eq_path, norm_img)
        i += 1
