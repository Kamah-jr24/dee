import CV2
import numpy as np
url="Your IPAdress/video"
cp=CV2.VideoCapture(url)
while (True):
    camera,frame=cap.read()
    if frame is not None: