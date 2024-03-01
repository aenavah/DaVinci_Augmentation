# Device Image Augmentation

## User Inputs:

- base: local git repository path
- image_folder_root: name of folder with images to run (made by user)

### Directory Tree

Use same naming and structure from Dropbox so we can easily locate the images in the database

- I create a folder with the directory name from the dropbox (e.g. 20221104-20221118 Swine Expt-5), find the first subdirectory (e.g. Exp_5_Wound Picture from device camera) and download that entire subdirectory into the folder. The script only looks for .jpg and .img extensions, but this saves the script from iterating through extra data.

```plaintext
base
|-- image_folder_root\
|  |-- Dropbox Structure\...\woundimage.jpg
```

## Output Directory Tree

```plaintext
base
|-- image_folder_root\
|  |-- Dropbox Structure\...\woundimage.jpg
|-- cropped_images_root #holds images with lights removed
|-- patch_images_root #image patches
|-- augm_folder_root
|  |Dropbox Structure\...\Full
|  |  |seed folders\
|  |Dropbox Structure\...\Patch
|  |  |seed folders\
```
