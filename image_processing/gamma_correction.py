import os
import cv2
import numpy as np


def gamma_correct_dataset(imDir, gammaDir, gamma, thresh=255):
    """Performs gamma correction on a given dataset

    Arguments:
        imDir {String} -- Path to the directory containing the image dataset
        gammaDir {String} -- Path of directory to save filtered dataset
        gamma {float} -- gamma value to use in the correction

    Keyword Arguments:
        thresh {int} -- Only processes images with mean intensities below
                        thresh (default: {255})
    """
    # build a lookup table mapping the pixel values [0, 255] to
    # their adjusted gamma values
    inv_gamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
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
        img_gamma_path = f'{gammaDir}/{img_file}'
        # Load each image
        img = cv2.imread(img_path)
        # Convert to HSV
        img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
        # Check if mean intensity is less than the threshold
        if np.mean(img_hsv[:, :, 2]) <= thresh:
            n += 1
            # perform gamma correction
        img_gamma = cv2.LUT(img, table)
        # convert image back from HSV to RGB
        img_gamma = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2RGB)
        # Save equalized image to eqDir using the same filename
        cv2.imwrite(img_gamma_path, img_gamma)
        i += 1
    print(f'{n} images enhanced!')
