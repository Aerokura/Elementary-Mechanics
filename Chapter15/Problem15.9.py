import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import sympy as sym
import math
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation # 动画
g = 9.81 # m/s^2 
L = 1 # m
m = 1 # kg
x10 = -L*math.cos(1/3*math.pi)
y10 = -L*math.sin(1/3*math.pi)
x20 = -x10
y20 = y10
xc0 = (x10+x20)/2
yc0 = (y10+y20)/2
theta0 = 0
vx0 = math.sqrt(3)/2*math.sqrt(math.sqrt(3)/2*g*L)
print(vx0)
omega = math.sqrt(math.sqrt(3)*g/(2*L))
ay = -g
ax = 0
dt = 0.001 #s
time = 2 #s
n = int(np.ceil(time/dt))
theta = np.zeros((n,1),float)
t = np.zeros((n,1),float)
r = np.zeros((n,2),float)
r1 = np.zeros((n,2),float)
r2 = np.zeros((n,2),float)
v = np.zeros((n,2),float)
a = np.zeros((n,2),float)
# Initial conditions
r[0,:] = np.array([xc0,yc0])
r1[0,:] = np.array([x10,y10])
r2[0,:] = np.array([x20,y20])
v[0,:] = np.array([vx0,0])
theta[0] = theta0
i = 0
for i in range(n-1):
    a[i,:] = np.array([ax,ay])
    v[i+1,:] = v[i,:]+a[i,:]*dt
    r[i+1,:] = r[i,:]+v[i+1,:]*dt
    theta[i+1] =  theta[i]+omega*dt
    t[i+1] = t[i]+dt 
    r1[i+1,0] = r[i+1,0]-0.5*L*math.cos(theta[i+1])
    r1[i+1,1] = r[i+1,1]-0.5*L*math.sin(theta[i+1])
    r2[i+1,0] = r[i+1,0]+0.5*L*math.cos(theta[i+1])
    r2[i+1,1] = r[i+1,1]+0.5*L*math.sin(theta[i+1])

# plt.subplot(3,1,1)
# plt.plot(r[0:i,0],r[0:i,1])
# plt.xlabel('$x_c$ [m]')
# plt.ylabel('$y_c$ [m]')
# plt.subplot(3,1,2)
# plt.plot(r1[0:i,0],r1[0:i,1])
# plt.xlabel('$x_1$ [m]')
# plt.ylabel('$y_1$ [m]')
# plt.subplot(3,1,3)
# plt.plot(r2[0:i,0],r2[0:i,1])
# plt.xlabel('$x_2$ [m]')
# plt.ylabel('$y_2$ [m]')
# plt.show()

fig, ax = plt.subplots()
ax.plot(r[0:i,0],r[0:i,1], 'k-', label='Center of Mass')
ax.plot(r1[0:i,0],r1[0:i,1], 'r:', label='$M_1$')
ax.plot(r2[0:i,0],r2[0:i,1], 'b--', label='$M_2$')
ax.grid()
plt.xlabel('x [m]')
plt.ylabel('y [m]')
legend = ax.legend(loc='upper right')

# Put a nicer background color on the legend.
#legend.get_frame().set_facecolor('C0')
plt.savefig("FigProblem5.9-2s.png",dpi=300)
plt.show()
# 间隔取数
inter = 20
def every_nth(lst,nth):
    return lst[nth - 1::nth]
xx = every_nth(r[0:i,0],inter)
xx1 = every_nth(r1[0:i,0],inter)
xx2 = every_nth(r2[0:i,0],inter)
yy = every_nth(r[0:i,1],inter)
yy1 = every_nth(r1[0:i,1],inter)
yy2 = every_nth(r2[0:i,1],inter)
# Animation
fig = plt.figure()
ax = plt.subplot(111)
ax.grid()
plt.gca().set_aspect('equal')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
dot, = ax.plot([], [], 'ro')#center of mass
line, = ax.plot([],[],'o-',lw=2)

def init():
    ax.set_xlim(-1,6)
    ax.set_ylim(-20,1)
    return line
def update(j):
    newx = [xx1[j],xx2[j]]
    newy = [yy1[j],yy2[j]]
    line.set_data(newx,newy)
    dot.set_data(xx[j],yy[j])
    return line
ani = animation.FuncAnimation(fig,update,range(1,len(xx)),init_func=init, interval=100)
#需预装imagemagick
ani.save('Project15.9.gif', writer='imagemagick', fps=100)
plt.show()
        
