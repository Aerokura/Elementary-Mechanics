# Edited by Dr.Mengying Zhang  zhangmengyingkd@163.com
# Updated on 25/03/2022
import numpy as np
import matplotlib.pyplot as plt
# 4.1.1 Example: Motion of a falling Tennis Ball
g = 9.8
t = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5])
y = 1.6 - 0.5*g*t**2
print (y)
np.transpose([t,y])

# high resolution data
[t,x] = np.loadtxt('Chapter4/data/fallingtennisball02.txt',usecols=[0,1],unpack=True)
plt.plot(t,x)
plt.xlabel('t [s]')
plt.ylabel('x [m]')
plt.show ()

#numerical derivatives
# page 55-56 plotting x(t) v(t) a(t)
n = len(x)
dt = t[1] - t[0]
v = np.zeros(n-1,float)# velocity
for i in range(n-1):
    v[i] = (x[i+1]-x[i])/dt
a = np.zeros(n-1,float)#acceleration
for i in range(n-1):
    a[i] = (v[i]-v[i-1])/dt
plt.subplot(3,1,1)
plt.plot(t,x)
plt.ylabel('x [m]')
plt.subplot(3,1,2)
plt.plot(t[0:n-1],v)
plt.ylabel('v [m/s]')
plt.subplot(3,1,3)
plt.plot(t[1:n-1],a[1:n-1])#less
plt.xlabel('t [s]')
plt.ylabel('a [m/$s^2$]')
plt.show ()

# plotting first 0.5s
selected = [x for x in t if x<=0.5]
imax = len(selected)
plt.subplot(3,1,1)
plt.xlim([0,0.5])
plt.plot(t[1:imax],x[1:imax])
plt.ylabel('x [m]')
plt.subplot(3,1,2)
plt.xlim([0,0.5])
plt.plot(t[1:imax],v[1:imax])
plt.ylabel('v [m/s]')
plt.subplot(3,1,3)
plt.xlim([0,0.5])
plt.plot(t[1:imax],a[1:imax])
plt.xlabel('t [s]')
plt.ylabel('a [m/$s^2$]')
plt.show ()

# compare with mathematical mode
y0 = 1.6 # m
vt = -g*t
yt = y0 - 0.5*g*t**2
plt.subplot(2,1,1)
plt.plot(t[0:imax],x[0:imax],'-r')
plt.plot(t[0:imax],yt[0:imax],'--b')
plt.xlabel('t [s]')
plt.ylabel('y [m]')
plt.subplot(2,1,2)
plt.plot(t[0:imax],v[0:imax],'-r')
plt.plot(t[0:imax],vt[0:imax],'--b')
plt.xlabel('t [s]')
plt.ylabel('v [m/s]')
plt.show ()
