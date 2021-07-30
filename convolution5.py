import argparse
import cv2
import numpy as np

my_parser = argparse.ArgumentParser()

my_parser.add_argument('--image', type=str)
my_parser.add_argument('--kernel_size', type=int)

args = my_parser.parse_args()

image = cv2.imread(args.image, cv2.IMREAD_GRAYSCALE)
#
# kernel = np.ones((3, 3), dtype=float) / 9
#
# result = cv2.filter2D(image, -1, kernel)
result = cv2.blur(image, (args.kernel_size, args.kernel_size))

cv2.imwrite('result.jpg', result)
cv2.imshow('output', result)
cv2.waitKey()
