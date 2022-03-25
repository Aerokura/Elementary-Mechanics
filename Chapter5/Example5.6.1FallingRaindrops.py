# Edited by Dr.Mengying Zhang  zhangmengyingkd@163.com
# Updated on 25/03/2022
# page 99, 5.6.1 Example: Falling Raindrops
import numpy as np
import matplotlib.pyplot as plt
import math

# physical variables
g = 9.81 
kv = 1.85e-7 # Nsm^-2
m = 5.2e-7 # kg
time = 20.0
dt = 0.001

# Initial conditions
v0 = 0.0
# Numerical initialization
n = int(round(time/dt))
v = np.zeros(n,float)
a = np.zeros(n,float)
t = np.zeros(n,float)
# Set inital values
v[0] = v0
# Integration loop
for i in range(n-1):
    a[i] = -g-(kv/m)*v[i]
    v[i+1] = v[i] +a[i]*dt
    t[i+1] = t[i]+dt

fig, (ax1,ax2) = plt.subplots(2,1)
fig.suptitle('Plot of v(t) and a(t) for the drop')
ax1.plot(t,v)
ax1.set_ylabel('v [m/s]')
ax2.plot(t[0:n-1],a[0:n-1])
ax2.set_xlabel('t [s]')
ax2.set_ylabel('a [m/$s^2$]')
plt.savefig("Fig510raindrop.png",dpi=120)
plt.show()

# Full model: symbolic solution
import sympy as sym
v = sym.Function('v')
from sympy.abc import t
from sympy.abc import g
from sympy.abc import u #terminal velocity
sym.dsolve(sym.Derivative(v(t),t)+g+g/u*v(t),v(t))
# Results: Eq(v(t), C1*exp(-g*t/u) - u)
