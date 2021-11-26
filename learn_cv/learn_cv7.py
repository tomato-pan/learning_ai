# 绘制直方图
import cv2
import matplotlib.pyplot as plt


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


if __name__ == '__main__':
    img = cv2.imread("/Users/panjwangsu.com/Desktop/panj_python/learning_ai/124.jpeg")
    # draw_hist(img)
    cv_draw_hist(img)
