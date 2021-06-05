from numpy import *
a=array([1+1j,2,3,4])

print(a.dtype)
# 实部
print(a.real)
# 虚部
print(a.imag)
a.imag = [1,3,4,5]
print(a)
# 复共轭
print(a.conj())
print(a.nbytes)
# numpy数组的基本类型：
'''
基本类型	可用的Numpy类型	备注
布尔型	bool	占1个字节
整型	int8, int16, int32, int64, int128, int	int 跟C语言中的 long 一样大
无符号整型	uint8, uint16, uint32, uint64, uint128, uint	uint 跟C语言中的 unsigned long 一样大
浮点数	float16, float32, float64, float, longfloat	默认为双精度 float64 ，longfloat 精度大小与系统有关
复数	complex64, complex128, complex, longcomplex	默认为 complex128 ，即实部虚部都为双精度
字符串	string, unicode	可以使用 dtype=S4 表示一个4字节字符串的数组
对象	object	数组中可以使用任意值
Records	void	
时间	datetime64, timedelta64	
'''
b = array([1,2.3,4/2,"sss",(1,2,3)],dtype=object)
print(b*2)
# 转换类型
c = array([-1,2,-3,4])
print(asarray(c,dtype=uint8) ,c.dtype)
print(c)
aa = c.view(uint8)
print(aa)
c[0]=2
print(aa)