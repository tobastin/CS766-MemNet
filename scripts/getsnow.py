import os
import shutil
import glob
import random

n = 3000
if os.path.isdir("./Data"):
    shutil.rmtree("./Data")
os.mkdir("./Data")
os.mkdir("./Data/gt")
os.mkdir("./Data/synthetic")

files = glob.glob("../DataSet/Snow100K/train/synthetic/*.jpg")
print(len(files))

find = random.sample(range(len(files)), n)

for i in find:
    os.system("cp "+files[i]+" ./Data/synthetic/.")
    os.system("cp ../DataSet/Snow100K/train/gt/"+files[i].split("/")[-1]+" ./Data/gt/.")



