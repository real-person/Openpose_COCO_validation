import os
import cv2


def equalize_dataset(imDir, eqDir):
    """Performs global histogram equalization on a given dataset

    Arguments:
        imDir {String} -- Path to the directory containing the image dataset
        claheDir {String} -- Path of directory to save filtered dataset

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
        img_eq_path = f'{eqDir}/{img_file}'
        # Load each image
        img = cv2.imread(img_path)
        # Convert to greyscale
        img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
        # Histogram equalisation on the V-channel
        img_hsv[:, :, 2] = cv2.equalizeHist(img_hsv[:, :, 2])
        # convert image back from HSV to RGB
        img_eq = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2RGB)
        # Save equalized image to eqDir using the same filename
        cv2.imwrite(img_eq_path, img_eq)
        i += 1
