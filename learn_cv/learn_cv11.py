# ROI 查找感兴趣区域
import cv2 as cv
import numpy as np

def roi_demo():
    src = cv.imread("/Users/panjwangsu.com/Desktop/panj_python/learning_ai/124.jpeg")
    cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
    cv.imshow("input image", src)
    face = src[200:350, 120:360]#脸部区域
    gray = cv.cvtColor(face, cv.COLOR_BGR2GRAY)#转灰色
    backface = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)#
    src[200:350, 120:360] = backface
    cv.imshow("new image", src)
    cv.waitKey(0)
    cv.destroyAllWindows()
