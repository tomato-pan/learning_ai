import cv2
import numpy as np

"""
腐蚀算法：变瘦
    用kernel，扫描图像的每一个像素；用kernel与其覆盖的二值图像做 “与” 操作；如果都为1，结果图像的该像素为1；否则为0.
    结果：使二值图像减小一圈
"""


def erode_demo(image):
    print(image.shape)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cv2.imshow("binary", binary)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    dst = cv2.erode(binary, kernel)
    cv2.imshow("erode", dst)


"""
膨胀算法：变胖
    用kernel，扫描图像的每一个像素；用kernel与其覆盖的二值图像做 “与” 操作；如果都为0，结果图像的该像素为0；否则为1.
    结果：使二值图像扩大一圈
"""


def dilate_demo(image):
    print(image.shape)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)
    cv2.imshow("binary", binary)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    dst = cv2.dilate(binary, kernel)

    cv2.imshow("dilate", dst)


# 开操作：先膨胀再腐蚀
def dilate_erode(image):
    print(image.shape)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    dst1 = cv2.dilate(binary, kernel)
    dst = cv2.erode(dst1, kernel)
    open1 = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    print(dst == open1)  # 每个像素点比较
    difference = cv2.subtract(dst, open1)
    print(not np.any(difference))
    print(difference)
    hi = np.hstack((binary, dst1, dst, open1))
    cv2.imshow("demo", hi)

def close_opt(image):
    print(image.shape)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    close1 = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
    hi = np.hstack((binary, close1))
    cv2.imshow("demo", hi)


if __name__ == "__main__":
    img = cv2.imread("/Users/panjwangsu.com/Desktop/panj_python/learning_ai/123.jpeg")
    cv2.namedWindow("input image", cv2.WINDOW_AUTOSIZE)
    dilate_erode(img)
    close_opt(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
