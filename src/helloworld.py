import cv2

image = cv2.imread('../img/like_lenna.png')


cv2.imshow('image window', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
