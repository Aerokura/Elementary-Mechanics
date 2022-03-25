import numpy as np
import matplotlib.pyplot as plt
import math
#page 80 projects, 4.31 Sliding on snow.
# frction motion
miu = 0.1
g = 9.8 #m/s^2
v0 = 5 #m/s
dt = 0.01 # s
n = 3000
vstar = 0.5  #m/s 
mius = 0.2 # static coefficient of friction
miud = 0.1 # dynamic codefficient o friction
vm = 1.5 # m/s
v3 = np.zeros(n,float)
a3 = np.zeros(n,float)
t3 = np.zeros(n,float)
miuv = np.zeros(n,float)
v3[0] = v0
def friction(speed):
    if speed>vm:
        mium = miud+(mius-miud)/(1+vm/vstar)
        miuv = mium/np.sqrt(speed/vm)
    else:
        miuv = miud+(mius-miud)/(1+speed/vstar)
    return(miuv)
def acceleration3(speed,frictionv):
    if(speed >0):
        a = -frictionv*g
    elif(speed==0):
        a = 0
    else:
        a = frictionv*g
    return (a)

for p in range(n):
    miuv[p] = friction(v3[p])
    a3[p] = acceleration3(v3[p],miuv[p])
    t3[p+1] = t3[p]+dt
    # Euler's method
    v3[p+1] = v3[p]+dt*a3[p]
    if(v3[p+1]>1e-4):
        continue
    else:
        break
print(p+1)
print(v3[p+1])
plt.plot(t3[0:p],v3[0:p])
plt.xlabel('t [s]')
plt.ylabel('v [m/s]') 
plt.title('t-v')  
print(t3[p+1]) 
plt.savefig('project431g.png',dpi=120)
plt.show()