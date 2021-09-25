# 数组排序
from numpy import *
import numpy as np

names = array(['bob', 'sue', 'jan', 'ad'])
weights = array([20.8, 93.2, 53.4, 61.8])
# 改变数组的值--weight.sort()
print(sort(weights))
# 不改变数组的值
ordered_indices = argsort(weights)
print(ordered_indices, weights[ordered_indices])
# a = array([[0.2, 0.1, 0.5],
#            [0.4, 0.8, 0.3],
#            [0.9, 0.6, 0.7]])
# print(sort(a))  # 行排列
# print(sort(a, axis=0))  # 列排列

# 数组对角线
a = arange(6)
print(a)
a.shape = 2, 3
print(a)
print(a.reshape(3, 2))
# 报错
# print(a.reshape(3,3))
# 新增二维数组维度
y=a[newaxis,newaxis,:]
print(y,shape(y))
# 矩阵的转置
print(a.transpose())
print(a.T)
# 多维转一维
print(a.flatten())
print(weights.tostring())
print(weights.tostring(order="F"))
ss = weights.tostring()
aaa = np.fromstring(ss)
print(aaa)