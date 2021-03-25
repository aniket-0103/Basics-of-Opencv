# Programme for Masking of a image

import cv2 as cv
import numpy as np

# Reading sample image

img = cv.imread('CHECKPOINT1.png', 1)

# Thresholding the image

_, th1 = cv.threshold(img, 200, 255, cv.THRESH_BINARY)

# Taking output after the process

cv.imshow("Sample Image", img)
cv.imshow("Masked Image", th1)

cv.waitKey(0)
cv.destroyAllWindows()