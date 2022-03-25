# Edited by Dr.Mengying Zhang  zhangmengyingkd@163.com
# Updated on 25/03/2022
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
u0 = 100 # m/s
R = 20 # m 
fig = plt.figure()
ax = fig.gca(projection='3d')
x, y, z = np.meshgrid(np.arange(-30,40,10),
                      np.arange(-30,40,10),
                      np.arange(0,2.4,0.6))
rr = (x**2+y**2+z**2)**0.5
print(rr)
exp2 = np.vectorize(math.exp)
wx = -u0*y*exp2(-rr/R)/R
wy = u0*x*exp2(-rr/R)/R
s = wx.shape
wz = np.zeros(np.array(s))
#print(wx.shape)
ax.quiver(x, y, z, wx, wy, wz)
plt.show()
