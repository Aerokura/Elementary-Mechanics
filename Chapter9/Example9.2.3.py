# Edited by Dr.Mengying Zhang  zhangmengyingkd@163.com
# Updated on 25/03/2022
# Page245 9.2.3 Example: Oscillations During an Earthquake
import numpy as np
import matplotlib.pyplot as plt
import math
#implement both dynamic and static friction in a numerical model of motion under friction.
#真实，粗糙的表面通常包含许多单个的凹凸-构成沿着表面的真实接触的小突起。在这里，我们将讨论地震期间一个这样的凹凸不平沿接触面的运动。该系统如图9.10所示。我们如何建立该系统的简化模型？在地震过程中，两个表面彼此相对移动时，粗糙会变形和滑动。我们为这种相互作用提供了一个非常简单的模型：我们将粗糙建模为一块质量为m的块，并用弹簧将其附着在顶表面上。刚度k。用力FN将块向下压到下面的表面上。弹簧的连接点x0跟随顶面的运动。我们将假设在地震期间，顶面（因此x0）以x0（t）= A sinωt的形式振动。找到粗糙的运动。

# parameter settings based on a cube asperity of of size 10 µm and density 2.0g/cm3
# Initialize
m = 2e-12 # kg
A = 0.1e-5 # m
k = 10.0 # N/m
N = 1e-4 # N
T = 0.01 # s
omega = 2*math.pi/T
time = 2*T
dt = time/1e5
n = int(np.round(time/dt))
mud = 0.2 # dyanmic friction
mus = 0.4 # static friction

# Variables
t = np.zeros(n,float)
x = np.zeros(n,float)
v = np.zeros(n,float)
f = np.zeros(n,float)
xx = np.zeros(n,float)
# Initial condition
x[0] = 0.0
v[0] = 0.0
for i in range(n-1):
    xx[i] = A*math.sin(omega*t[i])
    x0 = A*math.sin(omega*t[i])
    FD = -k*(x[i]-x0) # Force on the block
    if v[i] == 0.0: # Static friction
        f[i] = -FD
        if abs(f[i])>mus*N: # Slips
            f[i] = -np.sign(FD)*mud*N
    else: #Dynamic friction
        f[i] = -np.sign(v[i])*mud*N
    Fnet = FD+f[i]
    a = Fnet/m
    v[i+1] = v[i]+a*dt
    if (v[i]!=0) and (np.sign(v[i+1])!=np.sign(v[i])):
        v[i+1] = 0.0 # The block has stopped
    x[i+1] = x[i]+v[i+1]*dt
    t[i+1] = t[i]+dt

plt.subplot(2,1,1)
plt.plot(t[0:i],f[0:i],'k-')
plt.xlabel('t [s]')
plt.ylabel('f [N] ')
plt.subplot(2,1,2)
plt.plot(t[0:i],xx[0:i],':')
plt.plot(t[0:i],x[0:i],'k-')
plt.xlabel('t [s]')
plt.ylabel('x [m]')
plt.savefig("Fig911-A=1e-6.png",dpi=120)
plt.show ()

