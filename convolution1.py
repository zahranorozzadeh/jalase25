import cv2
import numpy as np

image = cv2.imread('galaxy/g1.jpg', cv2.IMREAD_GRAYSCALE)
kernel = np.ones((15, 15), dtype=float) / 225

# result = np.zeros(image.shape, dtype='uint8')
# for i in range(2, image.shape[0] - 2):
#     for j in range(2, image.shape[1] - 2):
#         small_image = image[i - 2:i + 3, j - 2:j + 3]
#         result[i, j] = np.sum(np.multiply(small_image, kernel))

result = cv2.filter2D(image, -1, kernel)
cv2.imwrite('result.jpg', result)
cv2.imshow('output', result)
cv2.waitKey()
