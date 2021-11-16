import time

import cv2
import numpy as np
t1 = time.time()
# 读取图片
item = cv2.imread("/Users/panjwangsu.com/Desktop/panj_python/learning_ai/123.jpeg")
# 平滑处理/均值滤波
# 内核
kernel = np.ones((3, 3), np.float32) / 9
dst = cv2.filter2D(item, -1, kernel)
# 方框滤波
r1 = cv2.boxFilter(item, -1, (2, 2), normalize=1)
# 高斯滤波
gauss = cv2.GaussianBlur(item, (3, 3), 0, 0)
# 中值滤波
mid = cv2.medianBlur(item,3)
hi = np.hstack((item, dst, r1, gauss,mid))
cv2.imshow("test", hi)
print(time.time()-t1)
cv2.waitKey(0)
cv2.destroyAllWindows()
