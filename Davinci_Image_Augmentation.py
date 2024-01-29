
import cv2
import os 
import os.path 
import numpy
import pandas as pd
from PIL import Image
import shutil

def subbest_dirs(root_dir): #might just read in count csv instead of doing this, when patch folders are already made it looks in those
  subs = []
  for root, dirs, files in os.walk(root_dir):
    if not dirs:
      subs.append(root)
  return subs

def create_output_folders(target_path, seed_list):
  for output_type in ["Patch", "Full"]:
    folder_path = target_path + "/" + output_type
    if not os.path.exists(folder_path): #if patch or full folder doesnt
      os.makedirs(folder_path)
      for seed in seed_list:
        os.makedirs(folder_path + "/" + "s" + str(seed))

def copy_directories(src, dst):
    os.makedirs(dst, exist_ok=True)
    for item in os.listdir(src):
        source_path = os.path.join(src, item)
        destination_path = os.path.join(dst, item)
        if os.path.isdir(source_path):
            copy_directories(source_path, destination_path)

if __name__ == "__main__":
  #begin user inputs
  exp_type = "Device"
  image_folder = "/Users/alexandranava/Desktop/DARPA/Tasks/DaVinci_Augmentation/Test Images"
  output_folder = "/Users/alexandranava/Desktop/DARPA/Tasks/DaVinci_Augmentation/Augmented Images"
  seed_list = [0, 1]

  print("Running...")
  #Creates directory for output if it doesnt exists 
  if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print("Created folder Augmented Images in " + output_folder)
    copy_directories(image_folder, output_folder) #copy directory tree to output folder
    image_folder = subbest_dirs(output_folder) #get lowest directories in output folder
    for folder in image_folder:
      create_output_folders(folder, seed_list) #make folders patch, full, and seeds inside 

  print("Output folder Augmented Images already exists...")

  


