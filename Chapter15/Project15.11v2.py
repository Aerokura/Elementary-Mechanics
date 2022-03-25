#Project15.11 Micro-electromechanical system
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import sympy as sym
import math
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation # 动画
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
time = 1#s
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
for i in range(n):
    t0 = t0+dt
    t.append(t0)
    angddot0 =-3*kappa/(22*M*L**2)*ang0+15*g*math.cos(ang0)/(22*L)
    angdot0 = angdot0+angddot0*dt
    angdot.append(57.3*angdot0)
    ang0 = ang0+angdot0*dt
    ang.append(57.3*ang0)
    
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
plt.savefig('Fig1511anglev2.png',dpi=300)
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
plt.savefig('Fig1511cmposv2.png',dpi=300)
plt.show()
#Animation
# 间隔取数
inter = 20
def every_nth(lst,nth):
    return lst[nth - 1::nth]
angi = every_nth(ang[0:i],inter)
x2 = 2*L*cos2(radians2(angi))# end point of the system
y2 = -2*L*sin2(radians2(angi))
x3 = 1.25*L*cos2(radians2(angi))# center of mass
y3 = -1.25*L*sin2(radians2(angi))


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
    time_text.set_text(time_template %(0.02*j))
    return line, time_text
ani = animation.FuncAnimation(fig,update,range(1,len(x2)),init_func=init, interval=100)
#需预装imagemagick
ani.save('Project15.11iv2.gif', writer='imagemagick', fps=100)
plt.show()


