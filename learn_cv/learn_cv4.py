# sobel算子+scharr算子
# 最好计算出abs(dx)+abs(dy),若同时计算他们相加的绝对值会导致细节丢失

import cv2
import numpy as np


def xy_sobel(img):
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=3)
    cv2.imshow("original", img)
    cv2.imshow("x", sobelx)
    cv2.waitKey(0)
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
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def scharr_xy(img):
    scharrx = cv2.Scharr(img, cv2.CV_64F, 1, 0)
    scharry = cv2.Scharr(img, cv2.CV_64F, 0, 1)
    scharrx = cv2.convertScaleAbs(scharrx)  # 转回uint8
    scharry = cv2.convertScaleAbs(scharry)
    scharrxy = cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0)
    cv2.imshow("original", img)
    cv2.imshow("xy", scharrxy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def laplacian(img):
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    laplacian = cv2.convertScaleAbs(laplacian)  # 转回uint8
    cv2.imshow("original", img)
    cv2.imshow("laplacian", laplacian)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def canny_xy(img):
    print(img.shape)
    r = cv2.Canny(img, 210, 220)
    cv2.imshow("original", img)
    cv2.imshow("result", r)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    img = cv2.imread("/Users/panjwangsu.com/Desktop/panj_python/learning_ai/123.jpeg", cv2.IMREAD_GRAYSCALE)
    # xy_sobel(img)
    canny_xy(img)
