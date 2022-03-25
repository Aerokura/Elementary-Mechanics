# Edited by Dr.Mengying Zhang(zhangmengyingkd@163.com).
# Updated on 25/03/2022
#Project15.11 Micro-electromechanical system
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import sympy as sym
import math
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation # for animation 动画
theta = sym.Function('theta')
t = sym.Symbol('t',real=True,positive=True)
k = sym.Symbol('k',real=True,positive=True)
l = sym.Symbol('l',real=True,positive=True)
m = sym.Symbol('m',real=True,positive=True)
G = sym.Symbol('G',real=True,positive=True)
print(sym.dsolve(sym.Derivative(theta(t),t,2)-3*k/(22*m*l**2)*theta(t)-15*G/(22*l),theta(t)))

#constants
M = 1#kg
L = 0.5#m
kappa = 280.77 #Nm
g = 9.81#kgm/s
time = 5#s
dt = 0.001
n = int(np.ceil(time/dt))
t = []
ang = []
angdot = []
angddot = []
# Initial condition
ang.append(0)
angdot.append(0)
angdot0 = 0
t0 = 0
ang0 = 0
i = 0
while (angdot[i]>=0):
    t0 = t0+dt
    t.append(t0)
    angddot0 =-3*kappa/(22*M*L**2)*ang0+15*g*math.cos(ang0)/(22*L)
    angdot0 = angdot0+angddot0*dt
    angdot.append(57.3*angdot0)
    ang0 = ang0+angdot0*dt
    ang.append(57.3*ang0)
    i = i+1
print(ang[i])
print(t0)
#plot
plt.subplot(2,1,1)
plt.plot(t[0:i],ang[0:i])
plt.xlabel('t [s]')
plt.ylabel('theta [$^o$]')
plt.subplot(2,1,2)
plt.plot(t[0:i],angdot[0:i])
plt.xlabel('t [s]')
plt.ylabel('$\omega [^o$/s]')
plt.savefig('Fig1511angle.png',dpi=300)
plt.show()
#motion
cos2 = np.vectorize(math.cos)
sin2 = np.vectorize(math.sin)
radians2 = np.vectorize(math.radians)
plt.subplot(3,1,1)
plt.plot(t[0:i],1.25*L*cos2(radians2(ang[0:i])))
plt.xlabel('t [s]')
plt.ylabel('x [m]')
plt.subplot(3,1,2)
plt.plot(t[0:i],np.ones(i)*L/2)
plt.xlabel('t [s]')
plt.ylabel('y [m]')
plt.subplot(3,1,3)
plt.plot(t[0:i],-1.25*L*sin2(radians2(ang[0:i])))
plt.xlabel('t [s]')
plt.ylabel('z [m]')
plt.savefig('Fig1511cmpos.png',dpi=300)
plt.show()
#Animation
x2 = 2*L*cos2(radians2(ang[0:i]))# end point of the system
y2 = -2*L*sin2(radians2(ang[0:i]))
x3 = 1.25*L*cos2(radians2(ang[0:i]))# center of mass
y3 = -1.25*L*sin2(radians2(ang[0:i]))
fig = plt.figure()
ax = plt.subplot(111)
ax.grid()
dot, = ax.plot([], [], 'ro')#center of mass
line, = ax.plot([],[],'o-',lw=2)
time_template = 'time = %.3fs'
time_text = ax.text(0.05,0.1,'',transform=ax.transAxes)

def init():
    ax.set_xlim(-0.1,1.2)
    ax.set_ylim(-0.5,0.5)
    time_text.set_text('')
    return line, time_text
def update(j):
    newx = [0,x2[j]]
    newy = [0,y2[j]]
    line.set_data(newx,newy)
    dot.set_data(x3[j],y3[j])
    time_text.set_text(time_template %(0.001*j))
    return line, time_text
ani = animation.FuncAnimation(fig,update,range(1,i),init_func=init, interval=100)
#需预装imagemagick Please install imagemagick in advance.
ani.save('Project15.11i.gif', writer='imagemagick', fps=100)
plt.show()


