import cv2 
import numpy as np

#new_height = 300
#new_width = 300

#det = np.zeros((new_height, new_width), dtype=np.uint8)

image = cv2.imread('../img/like_lenna.png')
image = cv2.resize(image, (500,500))

croped_image = image[200:300,200:300]
croped_image[:] = 200


# 이미지를 보여주는 명령어
cv2.imshow('Image Window', image)
#cv2.imshow('Image Window', image_small)

#print(image.shape)
#print(image_small.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()