import sys
import numpy as np
import cv2

from TrafficLight import findLight

video = cv2.VideoCapture('traffic.mp4')
success,image = video.read()
count = 0


show = False

while success:
    cv2.imwrite("test.jpg", image)
    result, modImage = findLight("red", show)
    if result :
=======
    if findLight() == True :
>>>>>>> beda58482e11fc5d0c19874e8bca398450b9b0db
        print("RED")
    else :
        print("NONE")
    count = count + 1
   
    success, image = video.read()
    if show:
        cv2.show("Filtered", modImage)
        if cv2.waitKey(33) == 27: 
		    break

video.release()
cv2.destroyAllWindows()
