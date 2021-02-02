# PyLab is a convenience module that bulk imports matplotlib. pyplot (for plotting) and NumPy (for Mathematics and working with arrays) in a single name space. Although many examples use PyLab, it is no longer recommended.
# import matplotlib
# from matplotlib import pylab
# from pylab import *
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5,5,1000)
f = np.exp(-x**2)
plt.plot(x,f)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

h = 0.001
df = np.zeros(1000,float)
for i in range(1000):
    df[i] = (np.exp(-(x[i]+h)**2)-np.exp(-(x[i]-h)**2))/(2*h)
plt.plot(x,df)
plt.xlabel('$x$')
plt.ylabel('$df(x)/dx$')
plt.show()