# 图像轮廓
import cv2
import numpy as np


def image_edge(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转化为二值化图像
    ret, binary = cv2.threshold(gray,115,255,cv2.THRESH_BINARY)
    contours,hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    image = img.copy()
    rr = cv2.drawContours(image,contours,-1,(0,222,127),1)
    cv2.imshow("original",img)
    cv2.imshow("contours",rr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    img = cv2.imread("/Users/panjwangsu.com/Desktop/panj_python/learning_ai/124.jpeg")
    image_edge(img)