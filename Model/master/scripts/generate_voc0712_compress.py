# -*- coding:utf-8 -*-
"""
将VOC2007和VOC2012图像数据集, 利用cv2.imwrite()函数保存图像时, quality factor为10, 20.
"""
import os
import cv2
import glob

if __name__ == '__main__':
    data_dir = "/home/apurbaa_juit/CS766-MemNet/Data/snow/Apr10_3K/gt"#"/home/ly/caffe-ssd/data/VOC0712"
    save_dir = "/home/apurbaa_juit/CS766-MemNet/datasets/gt"

    while 1:
        image_path = glob.glob(data_dir+ "/*.jpg")
        #print("Bastin : ",len(image_path))
        #print("Bastin : ",os.path.join(data_dir, filename, "JPEGImages/"))
        #print(image_path[0].split("/")[8]) # Get the name of images.
        
        
        for i in range(len(image_path)):
            image = cv2.imread(image_path[i], 0) # Gray image

            save_path = save_dir
            if not os.path.exists(save_path):
                os.makedirs(save_path)

            save_image_path = os.path.join(save_path, image_path[i].split("/")[-1])
            cv2.imwrite(save_image_path, image) # quality 10. 
        break
            # default is 95.
            #print("Bastin : ", save_image_path)
            #break
            #cv2.imwrite(save_image_path, image)
            #break
