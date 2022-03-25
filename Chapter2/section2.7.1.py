# Edited by Dr.Mengying Zhang  zhangmengyingkd@163.com
# Updated on 25/03/2022
# PyLab is a convenience module that bulk imports matplotlib. pyplot (for plotting) and NumPy (for Mathematics and working with arrays) in a single name space. Although many examples use PyLab, it is no longer recommended.
import matplotlib
from matplotlib import pylab
from pylab import *# might not work in your editor
x = linspace(-5,5,1000)
f = exp(-x**2)
plot(x,f)
xlabel('x')
ylabel('f(x)')
show()

h = 0.001
df = zeros(1000,float)
for i in range(1000):
    df[i] = (exp(-(x[i]+h)**2)-exp(-(x[i]-h)**2))/(2*h)
plot(x,df)
xlabel('$x$')
ylabel('$df(x)/dx$')
show()
