#!/bin/bash
# Script to extract COCO JSON file for each trained model
clear && clear
currentFolder=$PWD
echo $currentFolder

IMAGE_DIR=$1
ImType=$(basename ${IMAGE_DIR})

SHARED_FOLDER=$2
echo $SHARED_FOLDER
OPENPOSE_MODEL=$(basename ${SHARED_FOLDER})
OPENPOSE_MODEL=${OPENPOSE_MODEL^^}
EXPERIMENT=$(basename $(dirname ${SHARED_FOLDER}))

# Folder where openpose is installed 
OPENPOSE_FOLDER=$3

# Resolution settings
SCALE_NUMBER=$4
SCALE_GAP=$5
NET_RESOLUTION=$6

# Face
# IMAGE_DIR_FRGC="/home/gines/devel/images/frgc_val/"
# IMAGE_DIR_MPIE="/home/gines/devel/images/multipie_val/"
# IMAGE_DIR_FACE_MASK_OUT="/home/gines/devel/images/face_mask_out_val/"
# Hand
# IMAGE_DIR_HAND_DOME="/home/gines/devel/images/hand_dome_val/"
# IMAGE_DIR_HAND_MPII="/home/gines/devel/images/hand_mpii_val/"


echo "Paths"

# Body
JSON_FOLDER=${SHARED_FOLDER}/${SCALE_NUMBER}scale/
# JSON_FOLDER_4=${SHARED_FOLDER}4scales/
# Foot
JSON_FOLDER_foot=${SHARED_FOLDER}foot_/${SCALE_NUMBER}scale/
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
mkdir $JSON_FOLDER
# mkdir $JSON_FOLDER_4
# Foot
mkdir $JSON_FOLDER_foot
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


echo "Running OpenPose for each model"
MODEL_FOLDER=$(dirname $(dirname ${SHARED_FOLDER}))/
pwd
cd $OPENPOSE_FOLDER
echo $PWD

# Sorted in natural order (NAT sort)
for modelPath in `ls -v ${SHARED_FOLDER}/*.caffemodel`; do
    prototxtPath=$(dirname ${modelPath})/pose_deploy.prototxt
    modelName=$(basename ${modelPath})
    echo "Processing $modelName in $EXPERIMENT"

    finalJsonFile=${JSON_FOLDER}${modelName}_${SCALE_NUMBER}_${ImType}.json
    finalJsonFile_foot=${JSON_FOLDER_foot}${modelName}_${SCALE_NUMBER}_${ImType}.json
    temporaryJsonFile=${PWD}/temporaryJson_${EXPERIMENT}_${modelName}_${SCALE_NUMBER}.json
    temporaryJsonFileFoot=${PWD}/temporaryJson_${EXPERIMENT}_${modelName}_${SCALE_NUMBER}_foot.json

    OP_COMAND="bin/OpenPoseDemo.exe --model_pose ${OPENPOSE_MODEL} --prototxt_path ${prototxtPath} "
    OP_COMAND+="--caffemodel_path ${modelPath} --render_pose 0 --display 0 --cli_verbose 0.2 "
    OP_COMAND+="--write_coco_json ${temporaryJsonFile} --num_gpu -1 --image_dir ${IMAGE_DIR} "
    OP_COMAND+="--write_coco_json_variants 3 --net_resolution ${NET_RESOLUTION} "
    OP_COMAND+="--scale_number ${SCALE_NUMBER} --scale_gap ${SCALE_GAP}"
    echo $OP_COMAND

    # Body/foot 1 scale
    echo "Processing bodies/feet..."
    
    if [ -f $finalJsonFile ]; then
        echo "${SCALE_NUMBER}-scale body/foot model already exists."
    else
        # Run Openpose for body/foot processing
        $OP_COMAND --model_folder ""
        echo "Moving Temp JSON file... "
        # Move JSON to NAS after finished
        mv ${temporaryJsonFile} ${finalJsonFile}
        mv ${temporaryJsonFileFoot} ${finalJsonFile_foot}
    fi 

done

echo "Finished! Exiting script in 10 seconds..."
sleep 10s
echo " "
