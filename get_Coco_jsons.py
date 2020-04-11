import os
from shutil import move
from subprocess import Popen
from time import sleep

from config import config, net_resolutions
from helpers.natural_sort import natural_sort


def get_coco_jsons():
    """Get json results files for each model specified in config.py
    """
    # name of the experimental model folder
    experiment = os.path.basename(os.path.dirname(config['model_folder']))
    # From config.py
    scale_number = config['Scale_number']
    net_resolution = net_resolutions[experiment][scale_number]
    model_folder = config['model_folder']
    rest = config['GPU_rest']
    # Equal spacing of scales. e.i [1, 0.75, 0.5, 0.25] for scale_number of 4
    scale_gap = str(1 / scale_number)
    # Folders for storing json results
    json_folder = f'{model_folder}/{scale_number}scale/'
    json_folder_foot = f'{model_folder}/foot_{scale_number}scale/'
    # Create folders
    if not os.path.exists(json_folder):
        os.makedirs(json_folder)
    if not os.path.exists(json_folder_foot):
        os.makedirs(json_folder_foot)
    # Path to Openpose application
    if config['Windows Portable Demo']:
        openpose_app = os.path.join(
            config["openpose_folder"],
            'bin/OpenPoseDemo.exe')
    elif config['System'] == 'Windows':
        openpose_app = os.path.join(
            config["openpose_folder"],
            'build/x64/Release/OpenPoseDemo.exe')
    elif config['System'] == 'Linux' or config['System'] == 'Mac':
        openpose_app = os.path.join(
            config["openpose_folder"],
            'build/examples/openpose/openpose.bin')
    # Model name to be passed to the openpose application
    openpose_model = os.path.basename(model_folder).upper()
    # Path to users desktop. Used for storing temporary json files
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    # Sorted in natural order
    for model_name in natural_sort(os.listdir(model_folder)):
        # for each .caffemodel file
        if not model_name.endswith('.caffemodel'):
            continue
        # Path to pose_deploy.prototxt
        prototxt_path = f'{model_folder}/pose_deploy.prototxt'
        # Path to the .caffemodel file
        model_path = f'{model_folder}/{model_name}'
        print(f"Processing {model_name} in {experiment}")
        # Only test on datasets specitfied in config.py
        for test in config['Folders to test']:
            image_dir = f'{config["dataDir"]}/{test}'
            # Set paths for json output files.
            # Name json results according to model, scale number, and dataset
            final_json_file = os.path.join(
                json_folder,
                f'{model_name}_{scale_number}_{test}.json')
            final_json_file_foot = os.path.join(
                json_folder_foot,
                f'{model_name}_{scale_number}_{test}.json')
            temporary_json_file = os.path.join(
                desktop,
                f'temporaryJson_{model_name}_{scale_number}_{test}.json')
            temporary_json_file_foot = os.path.join(
                desktop,
                f'temporaryJson_{model_name}_{scale_number}_{test}_foot.json')
            if os.path.exists(final_json_file):
                print(f"{scale_number}-scale body/foot model already exists.")
            else:
                print("Processing bodies/feet...")
                # Openpose comand line arguments
                openpose_command = [
                        openpose_app,
                        '--model_pose', openpose_model,
                        '--prototxt_path', prototxt_path,
                        '--caffemodel_path', model_path,
                        '--render_pose', '0',
                        '--display', '0',
                        '--cli_verbose', '0.2',
                        '--write_coco_json', temporary_json_file,
                        '--num_gpu', '-1',
                        '--image_dir', image_dir,
                        '--write_coco_json_variants', '3',
                        '--net_resolution', net_resolution,
                        '--scale_number', str(scale_number),
                        '--scale_gap', scale_gap,
                        '--model_folder', "",
                    ]
                # Run Openpose for body/foot processing
                openpose = Popen(openpose_command)
                openpose.wait()
                print("Moving Temp JSON file... ")
                # Move JSON to final folder after finished
                move(temporary_json_file, final_json_file)
                move(temporary_json_file_foot, final_json_file_foot)
                print(f"""Finished generating results for:\n
                      Experiment: {experiment}\n
                      Model: {model_name}\n
                      Scales: {scale_number}\n""",
                      f"\nSleeping for {rest} seconds...")
                sleep(rest)


if __name__ == "__main__":
    get_coco_jsons()
