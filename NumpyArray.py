import time
import numpy as np
import pandas as pd
from PIL import Image

def convert_images_to_arrays_train(file_path, df):
    lst_imgs = [l for l in df['image']]
    print(lst_imgs)
    return np.array([np.array(Image.open(file_path + img)) for img in lst_imgs])

def save_to_array(arr_name, arr_object):
    return np.save(arr_name, arr_object)


if __name__ == '__main__':
    start_time = time.time()

    labels = pd.read_csv("testlabels.csv")
    print(labels)

    print("Writing Train Array")
    X_test = convert_images_to_arrays_train('Complete_test/', labels)

    print(X_test.shape)

    print("Saving Train Array")
    save_to_array('X_test.npy', X_test)

    print("--- %s seconds ---" % (time.time() - start_time))


