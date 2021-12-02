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


def logic_demo(img1, img2):
    dst = cv2.bitwise_and(img1, img2)
    dst1 = cv2.bitwise_or(img1, img2)
    no = cv2.bitwise_not(img1)
    cv2.imshow("and", dst)
    cv2.imshow("or", dst1)
    cv2.imshow("no", no)


def brightness_demo(img, c, b):
    h, w, ch = img.shape
    blank = np.zeros([h, w, ch], img.dtype)
    dst = cv2.addWeighted(img, c, blank, 1 - c, b)
    cv2.imshow("brightness", dst)


if __name__ == '__main__':
    m1 = cv2.imread("/Users/panjwangsu.com/Desktop/panj_python/learning_ai/124.jpeg")
    m2 = cv2.imread("/Users/panjwangsu.com/Desktop/panj_python/learning_ai/123.jpeg")
    img1 = cv2.resize(m1, (400, 400))
    img2 = cv2.resize(m2, (400, 400))
    print('src1均值：', cv2.mean(img1))
    print('src2均值：', cv2.mean(img2))
    add_demo(img1, img2)
    substract_demo(img1, img2)
    divide_demo(img1, img2)
    multiply_demo(img1, img2)
    logic_demo(img1, img2)
    brightness_demo(m1, 1, 0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
