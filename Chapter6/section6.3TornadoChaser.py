# Edited by Dr.Mengying Zhang  zhangmengyingkd@163.com
# Updated on 25/03/2022
# Page 161 discrete integration
import numpy as np
import matplotlib.pyplot as plt
import math

[t,x,y,z] = np.loadtxt('D:/My Teaching/备课材料/大学物理备课/编程/Chapter6/tornado.txt',usecols=[0,1,2,3],unpack=True)
n = len(t)
dt = t[1] - t[0]
a = np.zeros((n,3),float)
a[:,0] = x
a[:,1] = y
a[:,2] = z
v = np.zeros((n,3),float)
r = np.zeros((n,3),float)
r[0] = np.array([-80.0,0.0,0.0])
v[0] = np.array([184.9,-18.49,73.96])
for i in range(0,n-1):
    v[i+1] = v[i] + a[i]*dt
    r[i+1] = r[i] + 0.5*(v[i+1]+v[i])*dt#Euler-Cromer method
    t[i+1] = t[i] + dt
ddt = 1.0
it = np.round(ddt/dt)

plt.plot(r[1:i,0],r[1:i,1],'o')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.show()
