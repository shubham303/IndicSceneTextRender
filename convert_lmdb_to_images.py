import os

import cv2
import fire
import lmdb
import numpy as np
import six
from PIL import Image
import matplotlib as plt

# Wei Yang 2015-08-19
# Source
#   Read LevelDB/LMDB
#   ==================
#       http://research.beenfrog.com/code/2015/03/28/read-leveldb-lmdb-for-caffe-with-python.html
#   Plot image
#   ==================
#       http://www.pyimagesearch.com/2014/11/03/display-matplotlib-rgb-image/
#   Creating LMDB in python
#   ==================
#       http://deepdish.io/2015/04/28/creating-lmdb-in-python/



def generate_images(lmdb_file_path, out_dir):
    env = lmdb.open(
        lmdb_file_path,
        max_readers=32,
        readonly=True,
        lock=False,
        readahead=False,
        meminit=False)
   
    os.mkdir("{}/data/".format(out_dir))
    f = open("{}/gt.txt".format(out_dir), "w")
    with env.begin(write=False) as txn:
        n_samples = int(txn.get('num-samples'.encode()))
        for index in range(n_samples):
            idx = index + 1  # lmdb starts with 1
            label_key = 'label-%09d'.encode() % idx
            image_key = 'image-%09d'.encode() % idx
            
            label = txn.get(label_key).decode('utf-8')
            imgbuf = txn.get(image_key)
            buf = six.BytesIO()
            buf.write(imgbuf)
            buf.seek(0)
            img = Image.open(buf).convert('RGB')  # for color image
            img = np.array(img)
            cv2.imwrite("{}/data/{}.jpg".format(out_dir, index), img)
            f.write("data/{}".format(index))
            f.write("\t {}".format(label))
            f.write("\n")
            


if __name__ == '__main__':
	fire.Fire(generate_images)


