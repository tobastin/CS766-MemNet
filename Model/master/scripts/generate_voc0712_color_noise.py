import os
import glob
import cv2
import numpy as np
from skimage.util import random_noise
if __name__ == '__main__':
    #data_dir = "/home/apurbaa_juit/CS766-MemNet/Data/VOC0712/VOC2007"
    #data_dir = "/Users/parulgupta/MemNet-Tensorflow-GPU/data/Set2testkit/SingleColor"
    #save_path = "/home/apurbaa_juit/CS766-MemNet/datasets/VOC0712noise"
    #save_path = "/Users/parulgupta/cv766Proj/MemNet-Tensorflow/datasets/Set2TestNoiseVOC2007120"

    data_dir = "/home/apurbaa_juit/CS766-MemNet/Data/snow/Apr10_3K/gt"
    save_path = "/home/apurbaa_juit/CS766-MemNet/datasets/colorNoise"

    if not os.path.exists(save_path):
        os.makedirs(save_path)
    for image_file in glob.glob(os.path.join(data_dir, "*.jpg")):
        image = cv2.imread(image_file) # Color image
        save_image_path = os.path.join(save_path, image_file.split("/")[-1])
        print("Path :", save_image_path)
        # Add salt-and-pepper noise to the image.
        noise_img = random_noise(image, mode='s&p', amount=0.1)
        # The above function returns a floating-point image
        # on the range [0, 1], thus we changed it to 'uint8'
        # and from [0,255]
        noise_img = np.array(255*noise_img, dtype = 'uint8')
        # Display the noise image
        cv2.imwrite(save_image_path, noise_img)
