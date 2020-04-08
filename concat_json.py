import argparse
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("output_filename", 
                        help="name of the concatinated json file",
                        type=str)
    parser.add_argument("input_filenames", 
                        help="names of the json file to concatinate",
                        type=str)
    args = parser.parse_args()
    cat_json(args.output_filename, args.input_filenames)


def cat_json(output_filename, input_filenames):
    with open(output_filename, "w") as outfile:
        first = True
        for infile_name in input_filenames.split(","):
            with open(infile_name, "r") as infile:
                if first:
                    outfile.write('[')
                    first = False
                else:
                    outfile.write(',')
                outfile.write(mangle(infile.read()))
            os.remove(infile_name)
        outfile.write(']')


def mangle(s):
    return s.strip()[1:-1]


if __name__ == "__main__":
    main()
    # cat_json('/c/Users/marsh/Desktop/test.json', '/c/Users/marsh/Desktop/temporaryJson_body_25_pose_iter_584000.caffemodel_1_002.json,/c/Users/marsh/Desktop/temporaryJson_body_25_pose_iter_584000.caffemodel_1_003.json,/c/Users/marsh/Desktop/temporaryJson_body_25_pose_iter_584000.caffemodel_1_004.json,/c/Users/marsh/Desktop/temporaryJson_body_25_pose_iter_584000.caffemodel_1_005.json')
