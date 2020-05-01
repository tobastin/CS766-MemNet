# -*- coding:utf-8 -*-
"""
将VOC2007和VOC2012图像数据集, 利用cv2.imwrite()函数保存图像时, quality factor为10, 20.
"""
import os
import cv2
import glob

if __name__ == '__main__':
    data_dir = "../data/VOCdevkit"#"/home/ly/caffe-ssd/data/VOC0712"
    save_dir = "../datasets/VOC0712_Resize"

    for filename in ["VOC2007", "VOC2012"]:
        image_path = glob.glob(os.path.join(data_dir, filename, "JPEGImages/*.jpg"))
        
        for i in range(len(image_path)):
            image = cv2.imread(image_path[i], 0) # Gray image

            save_path = os.path.join(save_dir, filename)
            if not os.path.exists(save_path):
                os.makedirs(save_path)

            save_image_path = os.path.join(save_path, image_path[i].split("/")[-1])
            # downscale image
            dimd = (int(image.shape[1]/3),int(image.shape[0]/3))
            dimu = (image.shape[1],image.shape[0])
            iscaled = cv2.resize(image, dimd, interpolation = cv2.INTER_AREA)
            iscaleu = cv2.resize(iscaled, dimu, interpolation = cv2.INTER_AREA)
            
            # generate scaled image
            cv2.imwrite(save_image_path, iscaleu)
            # default is 95.
            #cv2.imwrite(save_image_path, image)
            
