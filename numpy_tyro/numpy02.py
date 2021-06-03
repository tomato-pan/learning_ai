from numpy import *

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

lst1 = [[0, 1],[ 2, 3], [5, 4]]
b = array(lst1)
print(b[0:1],b[-1],b[-3],b[::2],b[1,1])
print(b.shape)
od = array([21000, 21180, 21240, 22100, 22400])
print(od[1:]-od[:-1])