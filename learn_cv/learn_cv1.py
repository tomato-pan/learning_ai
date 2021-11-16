import cv2
import numpy as np

# 读取图片
item = cv2.imread("/Users/panjwangsu.com/Desktop/panj_python/learning_ai/123.jpeg")
cv2.imshow("111",item)


# 平滑处理
 # 内核
kernel = np.ones((3,3),np.float32)/9
dst = cv2.filter2D(item,-1,kernel)
cv2.imshow("112",dst)
cv2.waitKey(0)