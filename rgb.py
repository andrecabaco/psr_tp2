import cv2

img=cv2.imread('divisaopintada.png')
cv2.namedWindow('a', cv2.WINDOW_NORMAL)
cv2.imshow('a',img)
cv2.waitKey(0)