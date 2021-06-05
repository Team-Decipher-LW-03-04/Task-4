import numpy as np
import cv2

img = np.zeros((400,400,3), dtype = "uint8")
cv2.circle(img, (200,200), 80, (255,0,0), -1)

cv2.imwrite("blue.jpg",img)

cv2.imshow('blue', img)
cv2.waitKey(10000)
cv2.destroyAllWindows()