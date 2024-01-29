import os 
import os.path 
import pandas as pd
from PIL import Image


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

def crop_image(img_folder, original_size, crop_dims, newsize):
  remove_updown, remove_leftright = crop_dims
  output_folder = img_folder.replace(image_folder_root, cropped_images_root)
  print(output_folder)
  crop_box = (remove_leftright, remove_updown, original_size[0] - remove_leftright, original_size[1] - remove_updown) #left and upper, right and lower #og dimnsions: 5344 × 4012 
  
  for img_name in os.listdir(img_folder):
    img_path = os.path.join(img_folder, img_name)
    if ".jpg" in str(img_path):
      with Image.open(img_path) as img:
        img_cropped = img.crop(crop_box)
        img_cropped_resized = img_cropped.resize(newsize)
        cropped_img_name = output_folder + "/cropped_" + img_name
        img_cropped_resized.save(cropped_img_name)
        #crop lights 


if __name__ == "__main__":
  #required inputs 
  global image_folder_root, cropped_images_root, patch_images_root 
  image_folder_root = "/Users/alexandranava/Desktop/DARPA/Tasks/DaVinci_Augmentation/Test Images"
  cropped_images_root = "/Users/alexandranava/Desktop/DARPA/Tasks/DaVinci_Augmentation/Cropped Images"
  patch_images_root = "/Users/alexandranava/Desktop/DARPA/Tasks/DaVinci_Augmentation/Patch Images"
  augm_folder_root = "/Users/alexandranava/Desktop/DARPA/Tasks/DaVinci_Augmentation/Augmented Images"
  seed_list = [0, 1]

  ####### to change criteria:
  original = (5344, 4012)
  crop_dims = (775, 1250) #remove from topbottom, remove from leftright
  newsize = (512, 512)
  ###


  print("Running...")
  #Creates directory for outputs if they don't exist
  if not os.path.exists(augm_folder_root):
    for path in [cropped_images_root, patch_images_root, augm_folder_root]:
      os.makedirs(path)
      copy_directories(path)
    output_image_folder = subbest_dirs(augm_folder_root) #get lowest directories in output folder
    for folder in output_image_folder:
      create_output_folders(folder, seed_list) #make folders patch, full, and seeds at lowest dir
  else:
    pass

  input_image_folders = subbest_dirs(image_folder_root)
  for img_folder in input_image_folders:
    crop_image(img_folder, original, crop_dims, newsize)
    break 

    #call cropping function for each image in input_folder
    #output images to cropped_output_folder

    #read in cropped images folder, 
    #call subbiestdir for cropped images
    #for each image in dir in subbiestdir:
      #call patching fcn and output to patch folder with naming "qx_img8383.jpg"
 

