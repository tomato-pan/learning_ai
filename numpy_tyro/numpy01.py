import numpy
import math
from matplotlib import pyplot,pylab

a = numpy.linspace(0, 2 * math.pi, 21)
# print(a)
b = numpy.sin(a)
# print(b)
# 使用numpy画出sin图形
# pyplot.plot(a, b)
# pyplot.show()


# a = numpy.array([ True,  True,  True,  True,  True,  True,  True,  True,  True,
#         True,  True, False, False, False, False, False, False, False,
#        False, False, False], dtype=bool)
# mask = b>=0

# pyplot.plot(a,b,'b-o',a,numpy.sin(2*a),"r-^")
# 画出离散点
# pyplot.scatter(a,b)
# 画出离散点-2
x= pylab.rand(200)
y= pylab.rand(200)
size = pylab.rand(200) * 30
color = pylab.rand(200)
# 多张图像figure
# pyplot.figure(1)
# pyplot.scatter(x, y, size, color)
# pyplot.colorbar()
# pyplot.figure(0)
# pyplot.plot(a, b)
# 多幅子图
pyplot.subplot(2,2,1)
pyplot.scatter(x, y, size, color)
pyplot.subplot(2,2,2)
pyplot.plot(a, b)
pyplot.grid()
pyplot.show()