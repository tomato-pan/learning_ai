import cv2

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
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
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
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    dst = cv2.dilate(binary, kernel)
    cv2.imshow("dilate", dst)


if __name__ == "__main__":
    img = cv2.imread("/Users/panjwangsu.com/Desktop/panj_python/learning_ai/123.jpeg")
    cv2.namedWindow("input image", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("input image", img)
    erode_demo(img)
    dilate_demo(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
