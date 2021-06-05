from numpy import *
from numpy.random import rand
b = array([[1,2,3],
           [4,5,6]])
# 求和的两种方法
print(sum(b),b.sum())
# 一维求和
print(sum(b,axis=0),b.sum(axis=0))
# 求乘积
print(b.prod())
a = rand(3,4)
# 最大最小值
print(a,a.min(),a.min(axis=0),a.max())
# 最大最小值的位置下标
print(a.argmax(),a.argmin())
# 均值
print(a.mean(),average(a))
# 标准差
c = array([1,1.2])
print(c.std())
# 限制数值在某个范围

