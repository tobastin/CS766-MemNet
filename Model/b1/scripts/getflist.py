

import os

flist = os.listdir("/home/apurbaa_juit/CS766-MemNet/Data/snow/Apr10_3K/synthetic")
f= open("/home/apurbaa_juit/CS766-MemNet/datasets/synthetic_snow.txt", "w")
for fname in flist:
     f.write(fname+"\n")
f.close()
#print(flist[:5])
