import cv2
import numpy as np

image = cv2.imread('building.tif', cv2.IMREAD_GRAYSCALE)
kernel = np.array([[1, 0, -1],
                   [1, 0, -1],
                   [1, 0, -1]])

result = cv2.filter2D(image, -1, kernel)

cv2.imwrite('result.jpg', result)
cv2.imshow('output', result)
cv2.waitKey()
