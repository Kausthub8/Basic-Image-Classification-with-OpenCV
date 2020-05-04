import cv2
import numpy as np

def draw_circle(event, x, y, flags, param):
 if event== cv2.EVENT_LBUTTONDOWN:
  cv2.circle(img,(x,y),70,(35,69,70),-1)
        
        
cv2.namedWindow(winname='my_drawing')
        
cv2.setMouseCallback('my_drawing', draw_circle)
        
        
        
        
img = np.zeros((512,512,3), np.int8)
        
while True:
    
 cv2.imshow('my_drawing', img)
    
if cv2.waitKey(5) & 0XFF == 27: 
   sys.exit(0)
        
cv2.destroyALLWindows()
    
                
