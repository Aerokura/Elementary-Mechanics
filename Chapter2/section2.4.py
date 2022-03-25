# Edited by Dr.Mengying Zhang  zhangmengyingkd@163.com
# Updated on 25/03/2022
#from pylab import *
import matplotlib.pyplot as plt
import numpy as np
import math
n = int(math.ceil(10.0-0.0)/0.1+1)
x = np.zeros((n,1),float)
x[0] = 0.0
x[1] = 0.1
x[2] = 0.2
x[3] = 0.3
x[4] = 0.4
for i in range(n):
    x[i]=i*0.1
print(x)

#______Page16 for loops
x0 = 0.0
x1 = 10.0
dx = 0.1
n = int(math.ceil((x1-x0)/dx)+1)
x = np.zeros((n,1),float)
y = np.zeros((n,1),float)
for i in range(n):
    x[i] = x0+i*dx
    y[i] = math.sin(x[i])
plt.plot (x,y)
plt.show()

#______page 17 the while-loop
i = 0
while i<n:
    x[i] = x0 + i*dx
    y[i] = math.sin(x[i])
    i = i+1 #update the counter “manually” inside the loop

# falling ball hitting the ground   
t0 = 0.0
t1 = 10.0
dt = 0.1
n = int(math.ceil((t1-t0)/dt)+1)
t = np.zeros((n,1),float)
y = np.zeros((n,1),float)
t[0] = t0
y[0] = 100.0-4.9*t[0]**2
i = 0
while y[i]>0.0:
    i = i+1
    t[i] = t0+i*dt
    y[i] = 100.0-4.9*t[i]**2
#stopl
plt.plot(t[0:i],y[0:i])
plt.xlabel('t [s]')
plt.ylabel('y [m]')
plt.show()

#________Vectorization page18
del x
x = np.linspace(0,10,10)
print(x)
x1 = np.arange(0.0, 10.0, 0.3)
print(x1)
#the last number is 9.9 and not 10.0!
del y
y = np.zeros((np.size(x),1),float)
sin2 = np.vectorize(math.sin)
y = sin2(x)
plt.plot(x,y,'-')
#plt.show()

#________Vectorization page19
del x 
del y 
x = np.linspace(0,10,1000)
y = sin2(x)
plt.plot(x,y,':')
plt.show()

#_______
a = 1.0
exp2 = np.vectorize(math.exp)
f = x**2*exp2(-a*x)*sin2(math.pi*x)
plt.plot(x,f)
plt.show()
