from get_dataset import get_dataset
from get_Coco_jsons import get_coco_jsons
from evaluation import evaluate_jsons


def main():
    get_dataset()
    get_coco_jsons()
    evaluate_jsons()


if __name__ == "__main__":
    main()
