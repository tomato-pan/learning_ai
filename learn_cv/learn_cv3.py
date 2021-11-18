import cv2
import numpy as np


def top_hat_demo(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    dst = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)
    # 提升亮度
    cimage = np.array(gray.shape, np.uint8)
    cimage = 100
    dst = cv2.add(dst, cimage)
    cv2.imshow("top_hat_demo", dst)

def black_hat_demo(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    dst = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)
    # 提升亮度
    cimage = np.array(gray.shape, np.uint8)
    cimage = 100
    dst = cv2.add(dst, cimage)
    cv2.imshow("black_hat_demo", dst)

if __name__ == '__main__':
    img = cv2.imread("/Users/panjwangsu.com/Desktop/panj_python/learning_ai/123.jpeg")
    top_hat_demo(img)
    black_hat_demo(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()