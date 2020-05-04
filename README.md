# CS766-MemNet
 
Project based on : https://github.com/lyatdawn/MemNet-Tensorflow, http://cvlab.cse.msu.edu/pdfs/Image_Restoration%20using_Persistent_Memory_Network.pdf

# Installation

sudo apt-get install -y libsm6 libxext6 libxrender-dev
pip3 install opencv-python
pip3 install tensorflow     // v2.x
pip3 install tensorflow-gpu // v2.x 
pip3 install tensorboard 


# Datasets

* MemNet Dataset : http://host.robots.ox.ac.uk/pascal/VOC/voc2007/index.html
* DeSnow Dataset : https://sites.google.com/view/yunfuliu/desnownet
* DeRain Dataset : https://sites.google.com/view/yunfuliu/desnownet
* Kodak Color Dataset : http://r0k.us/graphics/kodak/


# codebase

* Model/master : based on MemNet baseline (M6R6)
* Model/b1 : updated model for M7R6
* Model/master/scripts : scripts for generating different usecase train/test data
