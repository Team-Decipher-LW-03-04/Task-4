import cv2
import numpy

photo = cv2.imread('img1.jpg')
dphoto = cv2.imread('img2.jpg')

cphoto = numpy.hstack((photo, dphoto))

cv2.imwrite("collage.jpg", cphoto)

cv2.imshow('joined photo', cphoto)
cv2.waitKey(9999)
cv2.destroyAllWindows()
