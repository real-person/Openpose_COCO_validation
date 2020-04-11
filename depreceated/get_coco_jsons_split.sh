#!/bin/bash
# Script to extract COCO JSON file for each trained model
clear && clear
currentFolder=$PWD
echo $currentFolder
# pass in command line argumet
subDir=$1
echo $subDir

echo "Parameters to change"
NUMBER_FOLDER=25
EXPERIMENT=1_25BSuperModel11FullVGG
# NUMBER_FOLDER=135
# EXPERIMENT=body_25
# Body/Foot
IMAGE_DIR="C:/Users/marsh/Pictures/COCO/val2017"
# Face
# IMAGE_DIR_FRGC="/home/gines/devel/images/frgc_val/"
# IMAGE_DIR_MPIE="/home/gines/devel/images/multipie_val/"
# IMAGE_DIR_FACE_MASK_OUT="/home/gines/devel/images/face_mask_out_val/"
# Hand
# IMAGE_DIR_HAND_DOME="/home/gines/devel/images/hand_dome_val/"
# IMAGE_DIR_HAND_MPII="/home/gines/devel/images/hand_mpii_val/"

echo "Common parameters to both files a_*.sh and b_*.sh"
# SHARED_FOLDER=C:/Users/marsh/Documents/GitHub/openpose_train/experimental_models/${EXPERIMENT}/body_${NUMBER_FOLDER}/
SHARED_FOLDER=C:/Users/marsh/Documents/GitHub/openpose_train/experimental_models/${EXPERIMENT}/body_${NUMBER_FOLDER}b/
# SHARED_FOLDER=/media/posefs3b/Users/gines/openpose_train/training_results/${EXPERIMENT}/pose/body_${NUMBER_FOLDER}d/
# SHARED_FOLDER=/media/posefs3b/Users/gines/openpose_train/training_results/${EXPERIMENT}/pose/body_${NUMBER_FOLDER}e/
# SHARED_FOLDER=/media/posefs3b/Users/gines/openpose_train/training_results/${EXPERIMENT}/pose/body_${NUMBER_FOLDER}n/
# SHARED_FOLDER=/media/posefs3b/Users/gines/openpose_train/training_results/${EXPERIMENT}/pose/body_${NUMBER_FOLDER}_x2/
echo " "

echo "Paths"
# OPENPOSE_MODEL=BODY_${NUMBER_FOLDER}
OPENPOSE_MODEL=BODY_${NUMBER_FOLDER}B
# OPENPOSE_MODEL=BODY_${NUMBER_FOLDER}E
OPENPOSE_FOLDER=C:/Users/marsh/Documents/School/Term_8/Engineering_in_Medicine/Motion_Tracking_Project/openpose-1.5.1-binaries-win64-gpu-python-flir-3d_recommended/openpose
# Body
JSON_FOLDER_1=${SHARED_FOLDER}1scale/
# JSON_FOLDER_4=${SHARED_FOLDER}4scales/
# Foot
JSON_FOLDER_1_foot=${SHARED_FOLDER}foot_1scale/
# JSON_FOLDER_4_foot=${SHARED_FOLDER}foot_4scales/
# Face
# JSON_FOLDER_1_frgc=${SHARED_FOLDER}frgc_1scale/
# JSON_FOLDER_4_frgc=${SHARED_FOLDER}frgc_4scales/
# JSON_FOLDER_1_mpie=${SHARED_FOLDER}mpie_1scale/
# JSON_FOLDER_4_mpie=${SHARED_FOLDER}mpie_4scales/
# JSON_FOLDER_1_faceMaskOut=${SHARED_FOLDER}faceMask_1scale/
# JSON_FOLDER_4_faceMaskOut=${SHARED_FOLDER}faceMask_4scales/
# Hand
# JSON_FOLDER_1_hand_dome=${SHARED_FOLDER}hand_dome_1scale/
# JSON_FOLDER_4_hand_dome=${SHARED_FOLDER}dome_4scales/
# JSON_FOLDER_1_hand_mpii=${SHARED_FOLDER}hand_mpii_1scale/
# JSON_FOLDER_4_hand_mpii=${SHARED_FOLDER}mpii_4scales/

# Create folders
# Body
mkdir $JSON_FOLDER_1
# mkdir $JSON_FOLDER_4
# Foot
mkdir $JSON_FOLDER_1_foot
# mkdir $JSON_FOLDER_4_foot
# Face
# mkdir $JSON_FOLDER_1_frgc
# mkdir $JSON_FOLDER_4_frgc
# mkdir $JSON_FOLDER_1_mpie
# mkdir $JSON_FOLDER_4_mpie
# mkdir $JSON_FOLDER_1_faceMaskOut
# mkdir $JSON_FOLDER_4_faceMaskOut
# Hand
# mkdir $JSON_FOLDER_1_hand_dome
# mkdir $JSON_FOLDER_4_hand_dome
# mkdir $JSON_FOLDER_1_hand_mpii
# mkdir $JSON_FOLDER_4_hand_mpii
echo " "

# echo "Sleeping for 8h..."
# sleep 27000
# echo "Awaken!"



# Different code than a_*.sh
echo "Running OpenPose for each model"
MODEL_FOLDER=$(dirname $(dirname ${SHARED_FOLDER}))/
pwd
cd $OPENPOSE_FOLDER
echo $PWD

# Sorted in natural order (NAT sort)
for modelPath in `ls -v ${SHARED_FOLDER}*.caffemodel`; do
# Not NAT sort
# for modelPath in ${SHARED_FOLDER}*.caffemodel; do
    prototxtPath=$(dirname ${modelPath})/pose_deploy.prototxt
    modelName=$(basename ${modelPath})
    echo "Processing $modelName in $EXPERIMENT"

    finalJsonFile1=${JSON_FOLDER_1}${modelName}_1_concat.json
    finalJsonFile1_foot=${JSON_FOLDER_1_foot}${modelName}_1_concat.json
    # temporaryJsonFiles=""
    # temporaryJsonFiles_foot=""'''

    #for subDir in `ls -v $IMAGE_DIR`; do
    temporaryJsonFile1=C:/Users/marsh/Desktop/temporaryJson_${EXPERIMENT}_${modelName}_1_${subDir}.json
    OP_COMAND="bin/OpenPoseDemo.exe --model_pose ${OPENPOSE_MODEL} --prototxt_path ${prototxtPath} --caffemodel_path ${modelPath} --render_pose 0 --display 0 --cli_verbose 0.2"
    OP_COMAND_1SCALE="${OP_COMAND} --write_coco_json ${temporaryJsonFile1} --num_gpu -1 "
    OP_COMAND_4SCALES="${OP_COMAND} --write_coco_json ${temporaryJsonFile4} --num_gpu -1"

    # Body/foot 1 scale
    echo "Processing bodies/feet..."
    temporaryJsonFile1Foot=C:/Users/marsh/Desktop/temporaryJson_${EXPERIMENT}_${modelName}_1_${subDir}_foot.json
    # if [ $subDir != '001' ]; then
    #     temporaryJsonFiles+=,
    #     temporaryJsonFiles_foot+=,
    # fi
    # temporaryJsonFiles+=$temporaryJsonFile1
    # temporaryJsonFiles_foot+=$temporaryJsonFile1Foot
    

    if [ -f $finalJsonFile1 ]; then
        echo "1-scale body/foot model already exists."
    else
        # Body/foot processing
        $OP_COMAND_1SCALE --image_dir ${IMAGE_DIR}/${subDir} --write_coco_json_variants 3 --model_folder "" --net_resolution -1x480
        # echo $subDir
    fi
        
        
    #done
    echo "Concatenating Temp JSON file... "
    cd $currentFolder
    echo $PWD
    # Move JSON to NAS after finished
    # python concat_json.py ${finalJsonFile1} ${temporaryJsonFiles}
    # python concat_json.py ${finalJsonFile1_foot} ${temporaryJsonFiles_foot}
    # mv ${temporaryJsonFile1Concat} ${finalJsonFile1}
    # mv ${temporaryJsonFile1Concat_foot} ${finalJsonFile1_foot}
done

echo "Finished! Exiting script in 10 secods..."
# Give GPU time to rest
sleep 10s
echo " "
