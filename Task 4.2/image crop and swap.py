import cv2
import numpy

dphoto = cv2.imread('img1.jpg')
photo = cv2.imread('img2.jpg')
cphoto = cv2.imread('img1.jpg')

dphoto[50:500, 100:400] , photo[50:500 , 100:400] = photo[50:500 , 100:400] , dphoto[50:500, 100:400]
photo[50:500 , 100:400] , cphoto[50:500 , 100:400] = cphoto[50:500 , 100:400] , photo[50:500 , 100:400]

cv2.imshow('hi', photo)
cv2.waitKey(9999)
cv2.destroyAllWindows()

cv2.imshow('hi', dphoto)
cv2.waitKey(9999)
cv2.destroyAllWindows()
