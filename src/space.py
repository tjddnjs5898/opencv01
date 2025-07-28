import cv2
import numpy as np

image = cv2.imread('../img/like_lenna.png')
image = cv2.resize(image, (500,500))

color = 255
image = cv2.rectangle(image, (250, 150), (340, 230), color, 5, 1)
image = cv2.rectangle(image, (370, 230), (450, 150), color, 5, 1)


cv2.imshow('line',image)

cv2.waitKey(0)
cv2.destroyAllWindows()