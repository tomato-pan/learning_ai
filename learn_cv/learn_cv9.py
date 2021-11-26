# numpy操作图像像素点
import cv2,time
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


if __name__ == '__main__':
    img = cv2.imread("/Users/panjwangsu.com/Desktop/panj_python/learning_ai/124.jpeg")
    # access_pixels(img)
    cv_inverse(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
