import cv2
import numpy as np

image = cv2.imread('Lenna.tif', cv2.IMREAD_GRAYSCALE)
kernel = np.array([[0, -1, 0]
                  , [-1, 8, -1]
                  , [0, -1, 0]], dtype=int)

result = np.zeros(image.shape, dtype='uint8')

for i in range(1, image.shape[0] - 1):
    for j in range(1, image.shape[1] - 1):
        small_image = image[i - 1:i + 2, j - 1:j + 2]
        result[i, j] = np.sum(np.multiply(small_image, kernel))

cv2.imshow('output', result)
cv2.waitKey()
