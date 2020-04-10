import os
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
# import numpy as np

from config import config
from get_dataset import annFile, annFile_foot


def evaluate_jsons(foot=False):
    """Prints the summary all the json results files for each model specified in config.py 
    
    Keyword Arguments:
        foot {bool} -- Set to True for foot keypoints results (default: {False})
    """
    # Generate list of tests that were done from config file
    tests = [config['dataType']]
    if config['Equalize']:
        tests.append('Equalized')
    if config['Normalize']:
        tests.append('Normalized')

    for test in config['Folders to test']:
        if foot:
            resFolder = config['model_folder'] + 'foot_1scale/'
            # initialize COCO ground truth api
            cocoGt = COCO(annFile_foot)
        else:
            resFolder = config['model_folder'] + '1scale/'
            # initialize COCO ground truth api
            cocoGt = COCO(annFile)

        resFilename = f'pose_iter_584000.caffemodel_1_{test}.json'
        resFile = os.path.join(resFolder, resFilename)
        print(resFile)

        # initialize COCO detections api
        cocoDt = cocoGt.loadRes(resFile)

        imgIds = sorted(cocoGt.getImgIds())
        # imgIds = imgIds[0:100]

        # running evaluation
        cocoEval = COCOeval(cocoGt, cocoDt, config['annType'])
        cocoEval.params.imgIds = imgIds
        cocoEval.evaluate()
        cocoEval.accumulate()
        print(f'Results for the {test} test:')
        cocoEval.summarize()


if __name__ == "__main__":
    evaluate_jsons(foot=False)
