from numpy import *
from  numpy.random import rand
lst = [0, 1, 2, 3, 5, 4]
a = array(lst)
print(a, type(a))
# 数组内数组类型
print(a.dtype)  # 元素类型
print(a.itemsize)  # 每个元素所占的字节
print(a.shape, shape(lst))  # 形状、每个元素代表一个维度
print(a.size)  # 所有元素所占的空间
print(a.ndim)  # 维度
a.fill(-3.8)  # 充满元素的值，此时由于类型是int32,所有填充的值就会被整型化
print(a,a[0])

# lst1 = [[0, 1],[ 2, 3], [5, 4]]
# b = array(lst1)
# print(b[0:1],b[-1],b[-3],b[::2],b[1,1])
# print(b.shape)
# od = array([21000, 21180, 21240, 22100, 22400])
# print(od[1:]-od[:-1])

c = array([[ 0, 1, 2, 3, 4, 5],
           [10,11,12,13,14,15],
           [20,21,22,23,24,25],
           [30,31,32,33,34,35],
           [40,41,42,43,44,45],
           [50,51,52,53,54,55]])
# 切片为引用机制，但b=a[2:4]时，改变b的值，就会改变a的值。
print(c[0,4:6])
print(c[4:,4:])
print(c[:,2])
# 申请分配新的内存，需要使用copy方法b=a[2:4].copy()

aa=rand(10)
print(aa)
mask = aa>0.5 # mask 必须为布尔数组
print(aa[mask])