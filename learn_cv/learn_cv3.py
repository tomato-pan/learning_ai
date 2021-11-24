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


def binary_top_hat(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    dst = cv2.morphologyEx(thresh, cv2.MORPH_TOPHAT, kernel)
    cv2.imshow("binary_top_hat", dst)


def binary_black_hat(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    dst = cv2.morphologyEx(thresh, cv2.MORPH_BLACKHAT, kernel)
    cv2.imshow("binary_black_hat", dst)


def gradient_fun(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    dst = cv2.morphologyEx(thresh, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow("gradient_fun", dst)
    edged = cv2.Canny(gray, 50, 210)  # Perform Edge detection
    cv2.imshow("edged", edged)


def gradient_ex_inter(image):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    dm = cv2.dilate(image, kernel)
    em = cv2.erode(image, kernel)
    dst1 = cv2.subtract(image, em)  # 内部梯度
    dst2 = cv2.subtract(dm, image)  # 外部梯度
    cv2.imshow("internal", dst1)
    cv2.imshow("external", dst2)


if __name__ == '__main__':
    img = cv2.imread("/Users/panjwangsu.com/Desktop/panj_python/learning_ai/123.jpeg")
    top_hat_demo(img)
    binary_top_hat(img)
    binary_black_hat(img)
    black_hat_demo(img)
    gradient_fun(img)
    gradient_ex_inter(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
