# Edited by Dr.Mengying Zhang  zhangmengyingkd@163.com
# Updated on 25/03/2022
import numpy as np
import matplotlib.pyplot as plt
import math
# 4.2 calculation of motion

#4.2.1 Modeling the motion of a falling tennis ball
# based on the sketch Fig. 4.9
D = 0.0245 # m^-1
g = 9.8 # m/s^2
y0 = 2.0
v0 = 0.0
time = 0.5
dt = 0.00001
# variables
n = math.ceil(time/dt)
y = np.zeros(n,float)
v = np.zeros(n,float)
a = np.zeros(n,float)
t = np.zeros(n,float)
# Initialize
y[0] = y0
v[0] = v0
# Euler-Cromer method
# Integration loop
for i in range(n-1):
    a[i] = -g-D*v[i]*abs(v[i])
    v[i+1] = v[i]+a[i]*dt
    y[i+1] = y[i]+v[i+1]*dt
    if (y[i+1]<0):
        break
    t[i+1] = t[i]+dt
print(v[i+1])
plt.subplot(3,1,1)
plt.plot(t[0:i],y[0:i])
plt.xlabel('t [s]')
plt.ylabel('y [m]')
plt.subplot(3,1,2)
plt.plot(t[0:i],v[0:i])
plt.xlabel('t [s]')
plt.ylabel('v [m/s]')
plt.subplot(3,1,3)
plt.plot(t[0:i-1],a[0:i-1])
plt.xlabel('t [s]')
plt.ylabel('a [$m/s^2$]')
plt.show ()

#symbolic solution
import sympy as sym
v = sym.Function('v') 
t = sym.Symbol('t',real=True,positive=True)
g = sym.Symbol('g',real=True,positive=True)
D = sym.Symbol('D',real=True,positive=True)
sym.dsolve(sym.Derivative(v(t),t)+g-D*v(t)**2,v(t))
sym.integrate(-(sym.sqrt(g)*sym.tanh(sym.sqrt(D*g)*t))/sym.sqrt(D),t) # compare with the answer on page 71
