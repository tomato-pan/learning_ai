# 像素逻辑运算
import cv2
import numpy as np


def logic_demo(img1, img2):
    dst = cv2.bitwise_and(img1, img2)
    dst1 = cv2.bitwise_or(img1, img2)
    no = cv2.bitwise_not(img1)
    cv2.imshow("and", dst)
    cv2.imshow("or", dst1)
    cv2.imshow("no", no)


if __name__ == '__main__':
    m1 = cv2.imread("/Users/panjwangsu.com/Desktop/panj_python/learning_ai/124.jpeg")
    m2 = cv2.imread("/Users/panjwangsu.com/Desktop/panj_python/learning_ai/123.jpeg")
    img1 = cv2.resize(m1, (400, 400))
    img2 = cv2.resize(m2, (400, 400))
    logic_demo(img1, img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
