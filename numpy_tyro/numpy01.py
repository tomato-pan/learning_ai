import numpy
import math
from matplotlib import pyplot,pylab
show = numpy.linspace(0,2*math.pi,21)
print(show)
b = numpy.sin(show)
print(b)

pyplot.plot(show,b)
pyplot.show()
