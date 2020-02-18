import os
import json
import matplotlib.pyplot as plt
import numpy as np
import cv2

from tqdm import tqdm

def save_json(list_file,path):
    with open(path,'w') as f:
        json.dump(list_file,f,indent=4)
    return 0

def load_jsonfile(json_path):
    with open(json_path, 'r', encoding="UTF-8") as f:
        json_file = json.load(f)
    return json_file

def main():
    load_path = '/Users/xujin/code/python_code/coco-analyze/annotations/person_keypoints_val2014.json'
    json_file = load_jsonfile(load_path)
    print(json_file)
    print(1)





if __name__ == '__main__':
    main()