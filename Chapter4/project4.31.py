import numpy as np
import matplotlib.pyplot as plt
import math
#page 80 projects, 4.31 Sliding on snow.
# frction motion
mu = 0.1
g = 9.8 #m/s^2
v0 = 5 #m/s
dt = 0.01 # s
n = 3000
v = np.zeros(n,float)
a = np.zeros(n,float)
t = np.zeros(n,float)
v[0] = v0

#(a)find the velocity v(t) of the block
def acceleration(speed):
    if(speed >0):
        a = -mu*g
    elif(speed ==0):
        a = 0
    else:
        a = mu*g
    return (a)

for i in range(n):
    a[i] = acceleration(v[i])
    t[i+1] = t[i]+dt
    v[i+1] = v[i]+dt*a[i]
    if(v[i+1]>1e-4):
       continue
    else:
        break
    print(i)
    print(v[i+1])

plt.plot(t[0:i],v[0:i])
plt.xlabel('t [s]')
plt.ylabel('v [m/s]')   
plt.title('t-v(simple model)')
plt.savefig("project431a.png",dpi=120)
plt.show ()
#(b) How long time does it take until the block stops?
# it depends on the way you define "stop"
# when vf = 1e-4 [m/s],tf =
print(t[i+1])     


#  (c) Write a program where you find v(t) numerically using Euler’s or Euler-Cromer’s
# method. (Hint: You can find a program example in the textbook.) Use the program
# to plot v(t) and compare with your analytical solution. Use a timestep of Δt = 0.01.       
v2 = np.zeros(n,float)
a2 = np.zeros(n,float)
t2 = np.zeros(n,float)
v2[0] = v0
vstar = 0.5  #m/s 
mus = 0.2 # static coefficient of friction
mud = 0.1 # dynamic codefficient o friction
def acceleration2(speed):
    # dry friction
    mu = mud+(mus-mud)/(1+speed/vstar)
    if(speed >0):
        a = -mu*g
    elif(speed==0):
        a = 0
    else:
        a = mu*g
    return (a)

for j in range(n):
    a2[j] = acceleration2(v2[j])
    t2[j+1] = t2[j]+dt
    # Euler's method
    v2[j+1] = v2[j]+dt*a2[j]
    if(v2[j+1]>1e-4):
        continue
    else:
        break
print(j)
print(v2[j+1])
plt.plot(t2[0:j],v2[0:j])
plt.xlabel('t [s]')
plt.ylabel('v [m/s]') 
plt.title('t-v(dry friction)')  
print(t2[j+1]) 
plt.savefig('project431c.png',dpi=120)
plt.show()

# (d) Show that the acceleration of the block when v>0:
plt.plot(t2[0:j],a2[0:j])
plt.title('t-a(dry friction)')
plt.xlabel('t [s]')
plt.ylabel('a [$m/s^2$]') 
plt.savefig('project431d.png',dpi=120)  
plt.show()

# (e) Use your program to find v(t) for the more realistic model, with the same starting velocity, and compare with your previous results. Are your results reasonable?
# Explain.
line1, = plt.plot(t[0:i],v[0:i],color ='b',label='simplified')
line2, = plt.plot(t2[0:j],v2[0:j],color = 'r',label='dry friction')
plt.title('Comparison between simple model and dry friction')
plt.xlabel('t [s]')
plt.ylabel('v [m/s]')   
plt.legend(handles = [line1,line2])
print(t2[j+1]) 
plt.savefig('project431e.png',dpi=120)
plt.show()

# (f) Show friction coefficient
nf = 200
velocity = np.zeros(n,float)
mum = np.zeros(n,float)
dh = 0.05
for k in range(nf-1):
    mum[k] = mud+(mus-mud)/(1+velocity[k]/vstar)
    velocity[k+1] = velocity[k]+dh
plt.plot(velocity[0:nf-1],mum[0:nf-1])
plt.xlabel('v [m/s]')
plt.ylabel('friction coefficient')
plt.title('friction coefficient(wet friction)')
plt.savefig('project431f.png',dpi=120)
plt.show()
# (g) Modify your program to find the time development of v for the block when
# vm = 1.5 m/s. Compare with the two other models above: The model without velocity
# dependence and the model for dry friction. Comment on the results.
mu = 0.1
g = 9.8 #m/s^2
v0 = 5 #m/s
dt = 0.01 # s
n = 3000
vstar = 0.5  #m/s 
mus = 0.2 # static coefficient of friction
mud = 0.1 # dynamic codefficient o friction
vm = 1.5 # m/s
v3 = np.zeros(n,float)
a3 = np.zeros(n,float)
t3 = np.zeros(n,float)
muv = np.zeros(n,float)
v3[0] = v0
def friction(speed):
    # friction model with velocity dependency
    if speed>vm:
        mum = mud+(mus-mud)/(1+vm/vstar)
        muv = mum/np.sqrt(speed/vm)
    else:
        muv = mud+(mus-mud)/(1+speed/vstar)
    return(muv)
def acceleration3(speed,frictionv):
    if(speed >0):
        a = -frictionv*g
    elif(speed==0):
        a = 0
    else:
        a = frictionv*g
    return (a)
for p in range(n):
    muv[p] = friction(v3[p])
    a3[p] = acceleration3(v3[p],muv[p])
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
plt.title('t-v(wet friction)')  
print(t3[p+1]) 
plt.savefig('project431g.png',dpi=120)
plt.show()
l1, = plt.plot(t[0:i],a[0:i],color ='b',label='simplified')
l2, = plt.plot(t2[0:j],a2[0:j],color = 'r',label='dry friction')
l3, = plt.plot(t3[0:p],a3[0:p],color ='g',label='wet friction')
plt.title('Comparison between three models')
plt.xlabel('t [s]')
plt.ylabel('a [$m/s^2$]')   
plt.legend(handles = [l1,l2,l3])
plt.title('Comparison of accelerations for three models')
print(t3[p+1]) 
plt.savefig('project431h-a.png',dpi=120)
plt.show()