# 向上取样 & 向下取样
# 会让图像失真：向下:删除所有偶数行与列;向上:在每个方向扩大为原来2倍，新增的行与列使用0填充
import cv2
import numpy as np


def pydown(img):
    r1 = cv2.pyrDown(img)
    r2 = cv2.pyrDown(r1)
    cv2.imshow("original", img)
    cv2.imshow("PyrDown1", r1)
    cv2.imshow("PyrDown2", r2)
    cv2.waitKey()
    cv2.destroyAllWindows()


def pyup(img):
    r1 = cv2.pyrUp(img)
    r2 = cv2.pyrUp(r1)
    cv2.imshow("original", img)
    cv2.imshow("PyrUp1", r1)
    cv2.imshow("PyrUp2", r2)
    cv2.waitKey()
    cv2.destroyAllWindows()


def lap_tri(img):
    # 拉普拉斯金字塔
    pass


if __name__ == '__main__':
    img = cv2.imread("/Users/panjwangsu.com/Desktop/panj_python/learning_ai/123.jpeg")

    pyup(img)
