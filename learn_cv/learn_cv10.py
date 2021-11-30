# 像素运算
import cv2
import numpy as np


def add_demo(img1, img2):
    print(img1.shape, img2.shape)  # 当且仅当图片长宽相等的情况下才可以相加
    dst = cv2.add(img1, img2)
    cv2.imshow("dst", dst)


if __name__ == '__main__':
    m1 = cv2.imread("/Users/panjwangsu.com/Desktop/panj_python/learning_ai/124.jpeg")
    m2 = cv2.imread("/Users/panjwangsu.com/Desktop/panj_python/learning_ai/124.jpeg")
    add_demo(m1, m2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
