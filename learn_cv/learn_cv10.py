# 像素运算
import cv2
import numpy as np


def add_demo(img1, img2):
    print(img1.shape, img2.shape)  # 当且仅当图片长宽相等的情况下才可以相加
    dst = cv2.add(img1, img2)
    cv2.imshow("add", dst)


def substract_demo(img1, img2):
    dst = cv2.subtract(img1, img2)
    cv2.imshow("substract", dst)


def divide_demo(img1, img2):
    dst = cv2.divide(img1, img2)
    cv2.imshow("divide", dst)


def multiply_demo(img1, img2):
    dst = cv2.multiply(img1, img2)
    cv2.imshow("multiply", dst)


if __name__ == '__main__':
    m1 = cv2.imread("/Users/panjwangsu.com/Desktop/panj_python/learning_ai/124.jpeg")
    m2 = cv2.imread("/Users/panjwangsu.com/Desktop/panj_python/learning_ai/123.jpeg")
    img1 = cv2.resize(m1, (400, 400))
    img2 = cv2.resize(m2, (400, 400))
    add_demo(img1, img2)
    substract_demo(img1, img2)
    divide_demo(img1, img2)
    multiply_demo(img1, img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
