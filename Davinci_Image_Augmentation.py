
import cv2
import os 
import numpy
import pandas as pd
from PIL import Image

def subbest_dirs(root_dir): #might just read in count csv instead of doing this, when patch folders are already made it looks in those
  subs = []
  for root, dirs, files in os.walk(root_dir):
    if not dirs:
      subs.append(root)
    print(subs) 
  return subs

def create_output_folders(target_path, seed_list):
  for output_type in ["Patch", "Full"]:
    folder_path = target_path + "/" + output_type
    if not os.path.exists(folder_path): #if patch or full folder doesnt
      os.makedirs(folder_path)
      for seed in seed_list:
        os.makedirs(folder_path + "/" + "s" + str(seed))
    if os.path.exists(folder_path):
      continue
     
  

if __name__ == "__main__":
  #begin user inputs
  exp_type = "Device"
  base = "/Users/alexandranava/Desktop/DARPA/Tasks/DaVinci_Augmentation/"
  # count_data_path = "/Users/alexandranava/Desktop/DARPA/Tasks/Count_Control_Images/Count Data/" + "Data_" + exp_type + "_V3.csv"
  # count_data_pd = pd.read_csv(count_data_path)
  # dropbox_paths = count_data_pd["Dropbox Path"].str.replace("Research and Data/Porcine Experiment at Davis/", "").to_list()
  # print(dropbox_paths[0])


  image_root = base + "Test Images"
  types = ["Patch", "Full"]
  seed_list = [0, 1]
  output_folders_exists = 0

  #end user inputs
  img_folders = subbest_dirs(image_root) #returns list of deepest folders in image_root
    for folder in img_folders: #for each folder in the list of deepest_folders
      create_output_folders(folder, seed_list)
  else:
    pass






