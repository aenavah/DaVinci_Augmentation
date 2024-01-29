
import cv2
import os 
import os.path 
import numpy
import pandas as pd
from PIL import Image
import shutil


#functions to initialize output directory
def subbest_dirs(root_dir):
  subs = []
  for root, dirs, files in os.walk(root_dir):
    if not dirs:
      subs.append(root)
  return subs
def copy_directories(src, dst):
    os.makedirs(dst, exist_ok=True)
    for item in os.listdir(src):
        source_path = os.path.join(src, item)
        destination_path = os.path.join(dst, item)
        if os.path.isdir(source_path):
            copy_directories(source_path, destination_path)
def create_output_folders(target_path, seed_list):
  for output_type in ["Patch", "Full"]:
    folder_path = target_path + "/" + output_type
    if not os.path.exists(folder_path): #if patch or full folder doesnt
      os.makedirs(folder_path)
      for seed in seed_list:
        os.makedirs(folder_path + "/" + "s" + str(seed))
        with open(folder_path + "/" + "s" + str(seed) + "/" + "info.txt", "w") as file:
          file.write("s" + str(seed) + " has value: " + str(seed))

if __name__ == "__main__":
  image_folder_root = "/Users/alexandranava/Desktop/DARPA/Tasks/DaVinci_Augmentation/Test Images"
  cropped_images_root = "/Users/alexandranava/Desktop/DARPA/Tasks/DaVinci_Augmentation/Cropped Images"
  patch_images_root = "/Users/alexandranava/Desktop/DARPA/Tasks/DaVinci_Augmentation/Patch Images"
  output_folder_root = "/Users/alexandranava/Desktop/DARPA/Tasks/DaVinci_Augmentation/Augmented Images"
  seed_list = [0, 1]

  print("Running...")
  #Creates directory for outputs if they don't exist
  if not os.path.exists(output_folder_root):
    for path in [cropped_images_root, patch_images_root, output_folder_root]:
      os.makedirs(path)
      copy_directories(path)
    output_image_folder = subbest_dirs(output_folder_root) #get lowest directories in output folder
    for folder in output_image_folder:
      create_output_folders(folder, seed_list) #make folders patch, full, and seeds at lowest dir
  else:
    pass

  input_image_folders = subbest_dirs(image_folder_root)
  for input_folder in input_image_folders:
    cropped_output_folder = input_folder.replace(image_folder_root, cropped_images_root) + "/" #goes in corresponding output folder, but not in path or full folder yet 



    #call cropping function for each image in input_folder
    #output images to cropped_output_folder

    #read in cropped images folder, 
    #call subbiestdir for cropped images
    #for each image in dir in subbiestdir:
      #call patching fcn and output to patch folder with naming "qx_img8383.jpg"
 

