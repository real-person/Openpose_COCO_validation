import os
import cv2
import numpy as np


def clahe_dataset(imDir, claheDir, clip_limit=2.0, grid_size=8,
                  thresh=255):
    """Performs contrast limited adaptive histogram equalization on a given dataset

    Arguments:
        imDir {String} -- Path to the directory containing the image dataset
        claheDir {String} -- Path of directory to save the filtered dataset

    Keyword Arguments:
        clip_limit {float} -- Contrast limit for each grid (default: {2.0})
        grid_size {int} -- size of the grid used for HE   (default: {8})
        thresh {int} -- Only processes images with mean intensities below
                        thresh (default: {255})
    """
    clahe = cv2.createCLAHE(clipLimit=clip_limit,
                            tileGridSize=(grid_size, grid_size))
    img_list = os.listdir(imDir)
    num_imgs = len(img_list)
    i = 1
    n = 0
    for img_file in img_list:
        if i % (num_imgs/5) == 0 or i == 1:
            print(f'Processing image {i}/{num_imgs}')
        # get image path
        img_path = f'{imDir}/{img_file}'
        # Create path for equalized image
        img_clahe_path = f'{claheDir}/{img_file}'
        # Load each image
        img = cv2.imread(img_path)
        # Convert to greyscale
        img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
        # create a CLAHE object (Arguments are optional).
        if np.mean(img_hsv[:, :, 2]) < 100:
            n += 1
            # Contrast Limited Adaptive Histogram Equalization on the V-channel
            img_hsv[:, :, 2] = clahe.apply(img_hsv[:, :, 2])
        # convert image back from HSV to RGB
        img_clahe = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2RGB)
        # Save equalized image to eqDir using the same filename
        cv2.imwrite(img_clahe_path, img_clahe)
        i += 1
    print(f'{n} images enhanced!')
