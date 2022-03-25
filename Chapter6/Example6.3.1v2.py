# Edited by Dr.Mengying Zhang  zhangmengyingkd@163.com
# Updated on 25/03/2022
# Page 168 Example 6.3.1 Feather in the wind
import numpy as np
import matplotlib.pyplot as plt
import math
# Physical constants
h = 10.0 # m
C = 30.0 # m^-1
w0 = 3.0 # m/s
b = 5.0 # m
g = 9.8 # m/s
# Numerical constants
time = 20.0
dt = 0.001
n = int(np.ceil(time/dt))
t = np.zeros((n,1),float)
r = np.zeros((n,2),float)
v = np.zeros((n,2),float)
a = np.zeros((n,2),float)



# Initial conditions
r[0,:] = np.array([0,h])
v[1,:] = np.array([0,0])

#Find the motion
for i in range(n-1):
    # wind speed model
    w = w0*(1.0-np.exp(-r[i,1]/b))*np.array([1,0])
    # Acceleration
    a[i,:] = -g*np.array([0,1])-C*np.linalg.norm(v[i,:]-w)*(v[i,:]-w)
    v[i+1,:] = v[i,:] + a[i,:]*dt
    r[i+1,:] = r[i,:] + v[i+1,:]*dt
    t[i+1] = t[i] + dt
    if r[i+1,1]<0:
        break

# Plot motion
plt.plot(r[0:i,0],r[0:i,1],'-k')

plt.axis('equal')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.show()
