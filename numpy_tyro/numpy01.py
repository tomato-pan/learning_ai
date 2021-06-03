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

# 画出离散点>=0
# a = numpy.array([ True,  True,  True,  True,  True,  True,  True,  True,  True,
#         True,  True, False, False, False, False, False, False, False,
#        False, False, False], dtype=bool)
# mask = b>=0

pyplot.plot(a,b,'b-o',a,numpy.sin(2*a),"r-^")
pyplot.show()