

import os

flist = os.listdir("../datasets/VOC0712/VOC2007")
f= open("../datasets/VOC0712.txt","w")
for fname in flist:
     f.write("VOC2007/"+fname+"\n")
f.close()
#print(flist[:5])
