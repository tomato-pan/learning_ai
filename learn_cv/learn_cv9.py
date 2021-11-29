# numpy操作图像像素点
import cv2, time
import numpy as np


def count_time(func):
    def wrap(img):
        t1 = time.time()
        func(img)
        print(time.time() - t1)

    return wrap


@count_time
def access_pixels(img):
    print(img.shape)
    height = img.shape[0]
    width = img.shape[1]
    channels = img.shape[2]
    print("width : %s, height : %s channels : %s" % (width, height, channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = img[row, col, c]
                img[row, col, c] = 255 - pv  # 取反操作
    cv2.imshow("demo", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


@count_time
def cv_inverse(img):
    dst = cv2.bitwise_not(img)
    cv2.imshow("dst", dst)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


def create_image():  # numpy 生成纯色图片
    img = np.zeros([400, 400, 3], np.int8)
    img[:, :, 0] = np.ones([400, 400]) * 215  # 修改第一通道的值
    img[:, :, 2] = np.ones([400, 400]) * 255  # 修改第一通道的值
    cv2.imshow("image", img)


def color_space_demo(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray", gray)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imshow("hsv", hsv)
    yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    cv2.imshow("yuv", yuv)
    Ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    cv2.imshow("ycrcb", Ycrcb)
    lower_red = np.array([10, 43, 46])
    upper_red = np.array([77, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    dst = cv2.bitwise_and(image, image, mask=mask)  # 除去mask部分的图像进行与运算。得到绿色
    cv2.imshow('hsvred', mask)
    cv2.imshow('dst', dst)
# 通道分离 b, g, r = cv2.split(src)#分离

if __name__ == '__main__':
    img = cv2.imread("/Users/panjwangsu.com/Desktop/panj_python/learning_ai/124.jpeg")
    color_space_demo(img)
    # create_image()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
