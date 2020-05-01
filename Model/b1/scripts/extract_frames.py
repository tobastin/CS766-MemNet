import cv2
import os
import shutil

if os.path.isdir("../videodata"):
    shutil.rmtree("../videodata")
os.mkdir("../videodata")
os.mkdir("../videodata/frames")

# Opens the Video file
cap= cv2.VideoCapture('../Video/video1.mp4')
outsize = (256,256)
#out = cv2.VideoWriter("../videodata/videogray.mp4",cv2.VideoWriter_fourcc('H','2','6','4'), 30, outsize)
out = cv2.VideoWriter("../videodata/videogray.mp4",cv2.VideoWriter_fourcc(*'mp4v'), 30, outsize)
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    
    #downscale to 256x256
    frame = cv2.resize(frame, outsize, interpolation = cv2.INTER_AREA)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.merge((frame,frame,frame))
    #print(frame.shape)
    out.write(frame)
    cv2.imwrite("../videodata/frames/kang"+str(i)+'.jpg',frame)
    
    i+=1
 
cap.release()
out.release()
#cv2.destroyAllWindows()