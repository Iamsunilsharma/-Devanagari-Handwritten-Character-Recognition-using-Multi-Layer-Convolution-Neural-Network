import os
import pandas as pd
import numpy as np


def get_lst_images(file_path):
    """
    Reads in all files from file path into a list.
    INPUT
        file_path: specified file path containing the images.
    OUTPUT
        List of image strings
    """
    return [i for i in os.listdir(file_path) if i != '.DS_Store']

if __name__ == '__main__':
   folder_names=get_lst_images('train'+'/')
   print(folder_names)
   df = pd.DataFrame({'image':[],'character':[]})
   for i, folder in enumerate(folder_names):
       lst_imgs=[]
       lst_imgs = get_lst_images('train/'+folder+'/')
       print(i,':',folder)
       for j,item in enumerate(lst_imgs):
           df = df.append([{'image':item,'character':i}],ignore_index=True)

print("Writing CSV")
df.to_csv('folderlabels.csv', index=False, header=True)
