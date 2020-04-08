import os
import zipfile
import urllib.request
import shutil

from config import config
from histogram_equalization import equalize_dataset
from normalization import normalize_dataset
from clahe import clahe_dataset
from selective_equalization import selective_clahe_dataset
from gamma_correction import gamma_correct_dataset


annType = config['annTypes'][2]      # specify type here
prefix = 'person_keypoints' if annType == 'keypoints' else 'instances'

# Setup data paths
dataDir = config['dataDir']
dataType = config['dataType']

annDir = f'{dataDir}/annotations'

imDir = f'{dataDir}/{dataType}'
eqDir = f'{dataDir}/Equalized'
normDir = f'{dataDir}/Normalized'

annZipFile = f'{dataDir}/instances_{dataType}.zip'
annZipFile_foot = f'{dataDir}/person_keypoints_val2017_foot_v1.zip'
imZipFile = f'{dataDir}/images_{dataType}.zip'
annFile = f'{annDir}/{prefix}_{dataType}.json'
annFile_foot = f'{annDir}/person_keypoints_val2017_foot_v1.json'
annURL = f'http://images.cocodataset.org/annotations/annotations_train{dataType}.zip'
annURL_foot = f'http://posefs1.perception.cs.cmu.edu/OpenPose/datasets/foot/person_keypoints_val2017_foot_v1.zip'
imURL = f'http://images.cocodataset.org/zips/{dataType}.zip'


def get_dataset():
    # Create folder for the annotations if it doesnt already exist
    if not os.path.exists(annDir):
        os.makedirs(annDir)
    # Create folder for the original dataset if it doesnt already exist
    if not os.path.exists(imDir):
        os.makedirs(imDir)
    # Create folder for the equalized dataset if it doesnt already exist
    if not os.path.exists(eqDir):
        os.mkdir(eqDir)
    # Create folder for the normalized dataset if it doesnt already exist
    if not os.path.exists(normDir):
        os.mkdir(normDir)

    # Download body annotations if not available locally
    if not os.path.exists(annFile):
        if not os.path.exists(annZipFile):
            print("Downloading zipped annotations to " + annZipFile + " ...")
            with urllib.request.urlopen(annURL) as r, \
                    open(annZipFile, 'wb') as o:
                shutil.copyfileobj(r, o)
            print("... done downloading.")
        print("Unzipping " + annZipFile)
        with zipfile.ZipFile(annZipFile, "r") as zip_ref:
            zip_ref.extractall(dataDir)
        print("... done unzipping")
    print("Will use annotations in " + annFile)

    # Download foot annotations if not available locally
    if not os.path.exists(annFile_foot):
        if not os.path.exists(annZipFile_foot):
            print(f"Downloading zipped annotations to {annZipFile_foot} ...")
            with urllib.request.urlopen(annURL_foot) as r, \
                    open(annZipFile_foot, 'wb') as o:
                shutil.copyfileobj(r, o)
            print("... done downloading.")
        print("Unzipping " + annZipFile_foot)
        with zipfile.ZipFile(annZipFile_foot, "r") as zip_ref:
            zip_ref.extractall(annDir)
        print("... done unzipping")
    print("Will use annotations in " + annFile_foot)

    if len(os.listdir(imDir)) == 0:
        if not os.path.exists(imZipFile):
            print("Downloading zipped images to " + imZipFile + " ...")
            with urllib.request.urlopen(imURL) as r, \
                    open(imZipFile, 'wb') as o:
                shutil.copyfileobj(r, o)
            print("... done downloading.")
        print("Unzipping " + imZipFile)
        with zipfile.ZipFile(imZipFile, "r") as zip_ref:
            zip_ref.extractall(dataDir)
        print("... done unzipping")
    print("Will use images in " + imDir)

    if config['Equalize']:
        if len(os.listdir(eqDir)) == 0:
            equalize_dataset(imDir, eqDir)

    if config['Normalize']:
        if len(os.listdir(normDir)) == 0:
            normalize_dataset(imDir, normDir)

    if config['CLAHE']:
        for clip_limit in config['CLAHE clip_limit']:
            for grid_size in config['CLAHE grid_size']:
                claheDir = f'{dataDir}/CLAHE_{clip_limit}_{grid_size}'
                if not os.path.exists(claheDir):
                    os.makedirs(claheDir)
                if len(os.listdir(claheDir)) == 0:
                    clahe_dataset(imDir, claheDir, clip_limit, grid_size)

    if config['CLAHE']:
        clip_limit = config['CLAHE clip_limit'][0]
        for grid_size in config['CLAHE grid_size'][:2]:
            mean_thresh = config['Mean intensity threshold']
            claheDir = f'{dataDir}/Selective_CLAHE_{clip_limit}_{grid_size}_{mean_thresh}'
            if not os.path.exists(claheDir):
                os.makedirs(claheDir)
            if len(os.listdir(claheDir)) == 0:
                selective_clahe_dataset(imDir, claheDir, clip_limit, grid_size)

    if config['Gamma']:
        for gamma in config['Gamma values']:
            gammaDir = f'{dataDir}/Gamma_{gamma}'
            if not os.path.exists(gammaDir):
                os.makedirs(gammaDir)
            if len(os.listdir(gammaDir)) == 0:
                gamma_correct_dataset(imDir, gammaDir, gamma)

    if config['Selective Gamma']:
        for gamma in config['Gamma values']:
            for thresh in config['Gamma threshold']:
                gammaDir = f'{dataDir}/Gamma_{gamma}_thresh_{thresh}'
                if not os.path.exists(gammaDir):
                    os.makedirs(gammaDir)
                if len(os.listdir(gammaDir)) == 0:
                    gamma_correct_dataset(imDir, gammaDir, gamma, thresh)


if __name__ == "__main__":
    get_dataset()
