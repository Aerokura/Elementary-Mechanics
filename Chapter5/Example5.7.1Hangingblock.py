# Edited by Dr.Mengying Zhang  zhangmengyingkd@163.com
# Updated on 25/03/2022
# page 112, 5.7.1 Example: Motion of a Hanging Block
import numpy as np
import matplotlib.pyplot as plt
import math

# Initialize
m = 1.0 # kg
k = 100.0 # N/m
v0 = 1.0 # in m/s
time = 2.0 # s
g = 9.8 # m/sˆ2
# Numerical setup
dt = 0.0001 # s
n = int(round(time/dt))
t = np.zeros(n,float)
y = np.zeros(n,float)
v = np.zeros(n,float)
# Initial values
y[0] = 0.0
v[0] = v0
# Simulation loop 
for i in range(n-1):
    F = -k*y[i] - m*g
    a = F/m
    v[i+1] = v[i] + a*dt
    y[i+1] = y[i] + v[i+1]*dt
    t[i+1] = t[i] + dt
fig, (ax1,ax2) = plt.subplots(2,1)
fig.suptitle('Illustration of block position and velocity')
ax1.plot(t,y,'-o')
ax1.set_ylabel('x [m]')
ax2.plot(t,v)
ax2.set_xlabel('t [s]')
ax2.set_ylabel('v [m/s]')
plt.savefig("Fig517springblock.png",dpi=120)
plt.show()
# for ii in range(n-1):
#     plt.subplot(2,1,1)
#     plt.plot(t,y,'-b',t[ii],y[ii],'ob')
#     plt.xlabel('t [s]')
#     plt.ylabel('y [m]')
#     plt.subplot(2,1,2)
#     plt.plot(t,v,'-b',t[ii],v[ii],'ob')
#     plt.xlabel('t [s]')
#     plt.ylabel('v [m/s]')
#____________________________________
# Visualisation
# from visual import *
# m = 0.1 # in kg
# k = 20.0 # in N/m
# d = 0.1 # in m
# x = 0.1
# v = 0.1
# # Initialize display
# L = 0.02
# H = 0.02,
# W = 0.02
# scene = display(x=0,y=0,width=800,height=400,center=(0.1,H/2,0.0),range=(0.1,0.1,0.1))
# ground = box(pos=(0.1,-0.001,0.0),size=(0.2,0.002,d))
# block = box(pos=(x,H/2,W/2),size=(L,H,W),color=color.blue)
# spring = helix(pos=(0,H/2,W/2),axis=(x-L/2,0,0),radius=H/4)
# while 1:
#     rate(100)
#     a = -k/m*(x-d)
#     v=v+ a*dt
#     x=x+ v*dt
#     block.x = x
#     spring.axis = (x - L/2,0.0,0.0)
#     if scene.mouse.clicked:
#         mc = scene.mouse.getclick()
#         x = mc.pos.x
#         print('x0 = ',x,',v0=',v)

import sympy as sym
y = sym.Function('y')
from sympy.abc import t
from sympy.abc import g
q = sym.Symbol('q',real =True, positive = True)#define a positive q
sym.dsolve(sym.Derivative(y(t),t,2)+g+q*y(t),y(t))
# RESULTS: Eq(y(t), C1*sin(sqrt(q)*t) + C2*cos(sqrt(q)*t) - g/q)


# Full model
# Initialize
m = 1.0 # kg
k = 100.0 # N/m
v0 = 0.0 # in m/s
time = 15.0 #
g = 9.8 # m/sˆ2
D = 2.5 # mˆ-1
vt = 0.2 # m/s
kv = D*vt
# Numerical setup
dt = 0.0001 # s
n = int(round(time/dt))
t = np.zeros(n,float)
y = np.zeros(n,float)
v = np.zeros(n,float)
# Initial values
y[0] = 0.0
v[0] = v0
# Simulation loop
for i in range(n-1):
    if (v[i]<vt):
        FD = -kv*v[i]
    else:
        FD = -D*v[i]*abs(v[i])# add air resistance 
    F = -k*y[i] - m*g + FD
    a = F/m
    v[i+1] = v[i] + a*dt
    y[i+1] = y[i] + v[i+1]*dt
    t[i+1] = t[i] + dt
fig, (ax1,ax2) = plt.subplots(2,1)
fig.suptitle('Plot of block position and velocity')
ax1.plot(t,y)
ax1.set_ylabel('x [m]')
ax2.plot(t,v)
ax2.set_xlabel('t [s]')
ax2.set_ylabel('v [m/s]')
plt.savefig("Fig519springblock.png",dpi=120)
plt.show()
