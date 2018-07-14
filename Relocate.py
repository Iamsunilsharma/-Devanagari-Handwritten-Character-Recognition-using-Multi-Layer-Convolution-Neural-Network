import os
import sys
# from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from skimage import io
from skimage.transform import resize
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def create_directory(directory):
    '''
    Creates a new folder in the specified directory if the folder doesn't exist.
    INPUT
        directory: Folder to be created, called as "folder/".
    OUTPUT
        New folder in the current directory.
    '''
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_lst_images(file_path):
    """
    Reads in all files from file path into a list.
    INPUT
        file_path: specified file path containing the images.
    OUTPUT
        List of image strings
    """
    return [i for i in os.listdir(file_path) if i != '.DS_Store']

def relocate(path, new_path):
    
    create_directory(new_path)
    dirs = [l for l in os.listdir(path) if l != '.DS_Store']
    total = 0
    
    folder_names=get_lst_images(path)
    print(folder_names)
    
    for i, folder in enumerate(folder_names):
        lst_imgs=[]
        lst_imgs = get_lst_images(path+folder+'/')
        for item in lst_imgs:
            img = io.imread(path+folder+'/'+item)
            io.imsave(str(new_path + item), img)
            total += 1
            print("Saving: ", item, total)


if __name__ == '__main__':
    relocate(path='test/', new_path='Complete_test/')
    
