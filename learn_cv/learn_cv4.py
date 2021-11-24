# sobel算子
# 最好计算出abs(dx)+abs(dy),若同时计算他们相加的绝对值会导致细节丢失

import cv2
import numpy as np


def xy_sobel(img):
    sobelx = cv2.Sobel(img, cv2.CV_64F,1,1,ksize=3)
    cv2.imshow("original", img)
    cv2.imshow("x", sobelx)
    cv2.waitKey()
    cv2.destroyAllWindows()

def xy_split_sobel(o):
    sobelx = cv2.Sobel(o, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(o, cv2.CV_64F, 0, 1, ksize=3)
    sobelx = cv2.convertScaleAbs(sobelx)  # 转回uint8
    sobely = cv2.convertScaleAbs(sobely)
    sobelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
    cv2.imshow("original", o)
    cv2.imshow("x", sobelx)
    cv2.imshow("y", sobely)
    cv2.imshow("xy", sobelxy)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    img = cv2.imread("/Users/panjwangsu.com/Desktop/panj_python/learning_ai/123.jpeg",cv2.IMREAD_GRAYSCALE)
    xy_sobel(img)
    # xy_split_sobel(img)
