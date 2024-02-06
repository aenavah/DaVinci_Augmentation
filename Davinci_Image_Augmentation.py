import os 
import os.path 
import pandas as pd
from PIL import Image, ImageDraw, ImageFilter
import torch as pt 
import numpy as np

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

def crop_resize_image(img_folder, original_size, crop_dims, newsize):
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

def make_patches(img_folder):
  output_folder = img_folder.replace(cropped_images_root, patch_images_root)
  #print(output_folder)
  for img_name in os.listdir(img_folder):
    img_path = os.path.join(img_folder, img_name)
    with Image.open(img_path) as img:
      width, height = img.size
      half_width, half_height = width // 2, height // 2
      #left, top, right, bottom
      quad_i = (0,0, half_width,half_height) #top_left
      quad_ii = (half_width, 0, width, half_height) #top_right
      quad_iii = (half_width, half_height, width, height) #bottom_right
      quad_iv = (0, half_height, half_width, height) #bottom_left
      quadrants = [quad_i, quad_ii, quad_iii, quad_iv]
      for quad in quadrants:
        if quad == quad_i:
          quadname = "quadi"
        if quad == quad_ii:
          quadname = "quadii"
        if quad == quad_iii:
          quadname= "quadiii"
        if quad == quad_iv:
          quadname = "quadiv"
        img_cropped = img.crop(quad)
        patch_img_name = output_folder + "/" + quadname +"_" + img_name

        #Add quadrant pixels onto image for debugging
        #draw = ImageDraw.Draw(img_cropped)
        #draw.text((10, 10), str(quad), fill="white")
        img_cropped.save(patch_img_name)
      ### cont from here 

def apply_blur(input_root, input_folder, output_root, seed, min_sigma, max_sigma):
  #needs to work for both patch and full 
  np.random.seed(seed)
  radius = np.random.uniform(min_sigma, max_sigma) #random amount of blur within specified range
  output_folder = input_folder.replace(input_root, output_root)
  print("hi------", output_folder)
  for img_name in os.listdir(input_folder):
    img_path = os.path.join(input_folder, img_name)
    if ".jpg" in img_path:
      #print(img_path)
      with Image.open(img_path) as img:
        blurred_img = img.filter(ImageFilter.GaussianBlur(radius))
        print("bye---------", img_name)
        #blurred_img.show()
        #blurred_img_name = output_folder + "/" + quadname +"_" + img_name

        break
      continue

if __name__ == "__main__":
  #-------------------------required inputs-------------------------
  global image_folder_root, cropped_images_root, patch_images_root 
  image_folder_root = "/Users/alexandranava/Desktop/DARPA/Tasks/DaVinci_Augmentation/Test Images"
  cropped_images_root = "/Users/alexandranava/Desktop/DARPA/Tasks/DaVinci_Augmentation/Cropped Images"
  patch_images_root = "/Users/alexandranava/Desktop/DARPA/Tasks/DaVinci_Augmentation/Patch Images"
  augm_folder_root = "/Users/alexandranava/Desktop/DARPA/Tasks/DaVinci_Augmentation/Augmented Images"
  seed_list = [0, 1] #testing, update later 

  ####### to change criteria:
  original = (5344, 4012) #size of original images
  crop_dims = (775, 1250) #remove from topbottom, remove from leftright
  newsize = (512, 512) #resize dims for cropped imgs 
  run_crop = 0 #0 if cropped exist
  run_patch = 0 #0 if patches made
  min_sigma = 4 #min blur
  max_sigma = 5 #max blur
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
  if run_crop == 1:
    #call cropping function for each image in input_folder >> cropped_output_folder
    for img_folder in input_image_folders:
      crop_resize_image(img_folder, original, crop_dims, newsize)

  cropped_images_folder = subbest_dirs(cropped_images_root)
  if run_patch == 1:
    for cropped_img_folder in cropped_images_folder:
      make_patches(cropped_img_folder)

  for cropped_img_folder in cropped_images_folder:
    apply_blur(cropped_images_root, cropped_img_folder, augm_folder_root, 0, min_sigma, max_sigma)

#next read in patches images and apply gausblur and save to aug folder
#read in full images from crop folder and apply gausblur
  

