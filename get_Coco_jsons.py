from subprocess import Popen
from time import sleep

from config import config
from get_dataset import dataDir


def get_coco_jsons():
    '''image_directories = [imDir]
    if config['Equalize']:
        image_directories.append(eqDir)
    if config['Normalize']:
        image_directories.append(normDir)'''
    for test in config['Folders to test']:
        image_folder = f'{dataDir}/{test}'
        shellscript = Popen(["git-bash.exe", "get_coco_jsons.sh", image_folder,
                            config['model_folder'], config['openpose_folder']])
        shellscript.wait()
        # Let GPU cool down between tests
        sleep(10)


if __name__ == "__main__":
    get_coco_jsons()
