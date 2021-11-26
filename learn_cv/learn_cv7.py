# 绘制直方图
import cv2
import matplotlib.pyplot as plt
import numpy as np


def draw_hist(img):  # plt绘制
    cv2.imshow("img", img)
    plt.hist(img.ravel(), 256)  # 将像素源转换为一位数组
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def cv_draw_hist(img):  # opencv 绘制 灰色直接[0]，BGR对应[0],[1],[2]
    histb = cv2.calcHist([img], [0], None, [256], [0, 255])
    histg = cv2.calcHist([img], [1], None, [256], [0, 255])
    histr = cv2.calcHist([img], [2], None, [256], [0, 255])
    plt.plot(histb, color='b')
    plt.plot(histg, color='g')
    plt.plot(histr, color='r')
    plt.show()


def cv_mask_hist(img):
    image = cv2.imread("/Users/panjwangsu.com/Desktop/panj_python/learning_ai/124.jpeg", cv2.IMREAD_GRAYSCALE)
    # image = cv2.cvtColor(img, cv2.IMREAD_GRAYSCALE) # 通过转化不行
    mask = np.zeros(image.shape, np.uint8)
    mask[100:200, 100:200] = 255
    histMI = cv2.calcHist([image], [0], mask, [256], [0, 255])
    hist = cv2.calcHist([image], [0], None, [256], [0, 255])
    plt.plot(hist, color='r')
    plt.plot(histMI)
    plt.show()
    # 计算掩膜相减的图像
    mask_img = cv2.bitwise_and(image, mask)
    cv2.imshow("r", image)
    cv2.imshow("mask", mask)
    cv2.imshow("mask_img", mask_img)
    cv2.waitKey()
    cv2.destroyAllWindows()


# 直方图均衡化
def hist_avg():
    img = cv2.imread("/Users/panjwangsu.com/Desktop/panj_python/learning_ai/124.jpeg", cv2.IMREAD_GRAYSCALE)
    equ = cv2.equalizeHist(img)
    plt.subplot(221)
    plt.imshow(img, cmap=plt.cm.gray), plt.axis('off')
    plt.subplot(222)
    plt.imshow(equ, cmap=plt.cm.gray), plt.axis('off')
    plt.subplot(223)
    plt.hist(img.ravel(), 256)
    plt.subplot(224)
    plt.hist(equ.ravel(), 256)
    plt.show()


if __name__ == '__main__':
    img = cv2.imread("/Users/panjwangsu.com/Desktop/panj_python/learning_ai/124.jpeg")
    # draw_hist(img)
    hist_avg()
