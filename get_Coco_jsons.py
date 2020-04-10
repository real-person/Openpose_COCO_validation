import os
from subprocess import Popen
from time import sleep

from config import config, net_resolutions


def get_coco_jsons():
    """Get json results files for each model specified in config.py
    """
    model = os.path.basename(os.path.dirname(config['model_folder']))
    scale_number = config['Scale_number']
    scale_gap = str(1 / scale_number)
    net_resolution = net_resolutions[model][scale_number]
    for test in config['Folders to test']:
        image_folder = f'{config["dataDir"]}/{test}'
        shellscript = Popen(["git-bash.exe", "get_coco_jsons.sh", image_folder,
                            config['model_folder'], config['openpose_folder'],
                            str(scale_number), scale_gap, net_resolution])
        shellscript.wait()
        # Let GPU cool down between tests
        # sleep(10)


if __name__ == "__main__":
    get_coco_jsons()
