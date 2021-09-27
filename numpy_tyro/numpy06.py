from numpy import *

a = array([[0, 1, 2, 3], [4, 5, 6, 7]])
print(a)
print(a.dtype)
print(a.shape)
print(a.size)
# 元素占用字节
print(a.itemsize)
# 全部占用字节
print(a.nbytes)
# 维度
print(a.ndim)
for i in a:
    print(i,type(i))
# 元素迭代器
for elt in a.flat:
    print (elt,type(elt))
print(a.flatten(), type(a.flatten()))
print(a.ravel(), type(a.ravel()))
print(a.resize((4,2)),a)
print(a.swapaxes(0,1))
# 转置
print(a.transpose())
print(a.T)
print(a.squeeze())
b = a.copy()
b[0][0]=-1
print(a)
print(b)
# 填充
b.fill(4)
print(b)
print(b.tolist(),type(b.tolist()))
print(b.tostring())
print(b.astype(float))
# 实数虚数
c = array([1+2j,3+4j,5+6j])
print(c.real)
print(c.imag)
print(c.conj())
print(c.conjugate())
print(c.sort())
print(c)