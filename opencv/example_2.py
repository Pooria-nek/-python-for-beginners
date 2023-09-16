import cv2 as cv
import numpy as np

img = cv.imread("jpg.jpg", cv.IMREAD_COLOR)

img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", img)

# define range of blue color in HSV
lower_yellow = np.array([15,50,180])
upper_yellow = np.array([40,255,255])

img2 = cv.inRange(img, lower_yellow, upper_yellow)

cv.imshow("img2", img2)

cv.imwrite("F:\image proccing\mini.jpg", img2)

cv.waitKey(0)
cv.destroyAllWindows()