# Edited by Dr.Mengying Zhang  zhangmengyingkd@163.com
# Updated on 25/03/2022
# Page 153 6.2.1 Example: Mars Express
import numpy as np
import matplotlib.pyplot as plt
import math
[t,x,y] = np.loadtxt('D:/My Teaching/备课材料/大学物理备课/编程/Chapter6/marsexpresslr.txt',usecols=[0,1,2],unpack=True)
n = len(t)
dt = t[1] - t[0]
r = np.zeros((n,2),float)
r[:,0] = x
r[:,1] = y
AU = 149598000.0
r = r/AU
plt.plot(r[:,0],r[:,1])
plt.axis('equal')
plt.xlabel('x [au]')
plt.ylabel('y [au]')
plt.show()

for i in range(1,n-1):
    plt.plot(r[i,0],r[i,1],'o')
    dr = (r[i+1,:] -r[i,:])-(r[i,:]-r[i-1,:])
    plt.quiver(r[i,0],r[i,1],dr[0],dr[1],angles='xy',scale_units='xy',scale=1)
plt.plot(r[:,0],r[:,1])
plt.axis('equal')
plt.xlabel('x [au]')
plt.ylabel('y [au]')
plt.savefig("Fig66a.png",dpi=120)
plt.show()



# high resolution
[t,x,y] = np.loadtxt('D:/My Teaching/备课材料/大学物理备课/编程/Chapter6/marsexpresshr.txt',usecols=[0,1,2],unpack=True)
n = len(t)
r = np.zeros((n,2),float)
r[:,0] = x
r[:,1] = y
AU = 149598000.0
r = r/AU
plt.plot(r[:,0],r[:,1])
plt.axis('equal')
plt.xlabel('x [au]')
plt.ylabel('y [au]')
plt.savefig("Fig66b.png",dpi=120)
plt.show()
dt = t[1]-t[0]
v = np.zeros((n,2),float)
vnorm = np.zeros(n,float)
anorm = np.zeros(n,float)
for i in range(n-1):
    v[i,:] = (r[i+1,:]-r[i,:])/dt
    vnorm[i] = np.linalg.norm(v[i,:])
a = np.zeros((n-1,2),float)
for i in range(1,n-1):
    a[i,:] = (v[i,:]-v[i-1,:])/dt
    anorm[i] = np.linalg.norm(a[i,:])

plt.subplot(2,1,1)
plt.plot(t[0:n-1], vnorm[0:n-1])
plt.xlabel('t [days]')
plt.ylabel('v [au/days]')
plt.subplot(2,1,2)
plt.plot(t[1:n-3],anorm[1:n-3])
plt.ylim((1e-4, 4e-4 ))
plt.xlabel('t [days]')
plt.ylabel('a [au/days$^2$]')
plt.savefig("Fig67.png",dpi=120)
plt.show ()
