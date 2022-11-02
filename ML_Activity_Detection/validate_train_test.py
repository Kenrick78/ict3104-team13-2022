from os import listdir
from os.path import isfile, join
import csv
import os
import shutil
from shutil import SameFileError
import json

import argparse

parser = argparse.ArgumentParser(description='Validate Video Files for training and testing')
parser.add_argument('-inputfilepath', type=str, help='specify input file path')
parser.add_argument('-outputfilepath',type=str, help='specify output file path')
parser.add_argument('-dataset',type=str,help="specify data compare file")




args = parser.parse_args()



RGB_filepath = args.inputfilepath
extracted_videos = args.inputfilepath
compare = args.dataset



"""
The validate_train_test opens the extracted N amount of features.

After feature extraction, use this PY file to create a standard JSON format file
for training and using the Pre-Trained PDAN model to learn new values FROM the extracted features

Expected Inputs Required:
- RGB+FLOW features (32)
- FLOW features

"""



onlyfiles = [f for f in listdir(extracted_videos) if isfile(join(extracted_videos, f))]

RGBFLOW_count = 0


rgb_flow_list = []
rgb_flow_list_rename = []
for i in onlyfiles:
  if i.__contains__("_rgb"):
    rgb_flow_list.append(i)
    rgb_flow_list_rename.append(i.replace("_rgb",""))
    RGBFLOW_count += 1
print("Total RGB+FLOW files extracted: " + str(RGBFLOW_count))



#Time to write them in a JSON format (for flow)
with open('videos.json', 'w', encoding='utf-8') as f:
     json.dump(rgb_flow_list, f, ensure_ascii=False, indent=4)
# print("rgb_flow.json generated")


src_folder = args.inputfilepath
dst_folder = args.outputfilepath


# printing the contents of the destination folder
# print("Destination folder before copying::", os.listdir(dst_folder))

# file names
total_count = 0
for i in rgb_flow_list:
  for x in rgb_flow_list_rename:
    src_file = src_folder + "/"+ i
    dst_file = dst_folder + "/"+ x
    if (total_count ==len(rgb_flow_list)):
      break

    try:
        # copy file
        shutil.copyfile(src_file, dst_file)
        # destination folder after copying
    except SameFileError:
        print("We are trying to copy the same File")
    except IsADirectoryError:
        print("The destination is a directory")
    total_count += 1
# print("Destination after copying", os.listdir(dst_folder))

# Now compare numpy files with Smarthome CS_json


# Opening JSON file
f = open(args.dataset)

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
# print(data.values())
backer_list = []
new_dict = {}
for i in rgb_flow_list_rename:
    backer_list.append(i.replace(".npy",""))
for i in backer_list:
    new_dict[i] = data.get(i)

with open('smarthome_CS_32.json', 'w', encoding='utf-8') as f:
    json.dump(new_dict, f, ensure_ascii=False)

print("Smarthome_CS_32.json has been generated")


# Closing file
f.close()



  