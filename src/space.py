import cv2
import numpy as np


image = cv2.imread('../img/like_lenna.png')
image = cv2.resize(image, (500, 500))


red_color = (0, 0, 255)


image = cv2.rectangle(image, (250, 150), (340, 230), red_color, 3, cv2.LINE_AA)


image = cv2.rectangle(image, (370, 150), (450, 230), red_color, 3, cv2.LINE_AA)


image = cv2.line(image, (340, 190), (370, 190), red_color, 3, cv2.LINE_AA)


cv2.imshow('line', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
