import os
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
# import numpy as np

from config import config, model_iters
from get_dataset import annFile, annFile_foot


def evaluate_jsons():
    """Prints the summary of the json results evaluated against the COCO
    annotations. (for each dataset specified in "Folders to test" in config.py)
    """
    # name of the experimental model folder
    experiment = os.path.basename(os.path.dirname(config['model_folder']))
    num_iters = model_iters[experiment]
    scales = config['Scale_number']
    # Iterate over datasets to evaluate
    for test in config['Folders to test']:
        if config['Foot']:
            resFolder = config['model_folder'] + '/foot_1scale/'
            # initialize COCO ground truth api
            cocoGt = COCO(annFile_foot)
        else:
            resFolder = config['model_folder'] + '/1scale/'
            # initialize COCO ground truth api
            cocoGt = COCO(annFile)

        resFilename = f'pose_iter_{num_iters}.caffemodel_{scales}_{test}.json'
        resFile = os.path.join(resFolder, resFilename)
        print(resFile)

        # initialize COCO detections api
        cocoDt = cocoGt.loadRes(resFile)

        # running evaluation
        cocoEval = COCOeval(cocoGt, cocoDt, config['annType'])
        cocoEval.evaluate()
        cocoEval.accumulate()
        print(f'Results for the {experiment} model on the {test} dataset:')
        cocoEval.summarize()


if __name__ == "__main__":
    evaluate_jsons()
