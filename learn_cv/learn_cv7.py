# 绘制直方图
import cv2
import matplotlib.pyplot as plt


def draw_hist(img):
    cv2.imshow("img", img)
    plt.hist(img.ravel(), 256)  # 将像素源转换为一位数组
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    img = cv2.imread("/Users/panjwangsu.com/Desktop/panj_python/learning_ai/124.jpeg")
    draw_hist(img)
