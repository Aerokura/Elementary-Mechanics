#page 410 13.2.4 Center of mass from image analysis
#复现书上例题“13.2.4 Example: Center of Mass from Image Analysis”的程序，处理图片可以直接从书上电子版截取，不同同学不需要相同，讨论滤镜选择的方式对形心判断的影响。
import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.image as mpimg
Q = mpimg.imread('./blank.png')# RGB #
print(Q.shape)
print(Q[0:2,0:2,0])
z = mpimg.imread('./ballimage02cut.png')# RGB 
print(type(z))
print(z.shape)
plt.subplot(1,2,1)
plt.imshow(z)
#plt.axis('equal')
z2 = (z[:,:,0]+z[:,:,1]+z[:,:,2])<1.5#去掉蓝光，剔除背景
print(type(z2))
print(z2.shape)
plt.subplot(1,2,2)
plt.imshow(z2)
s = np.shape(z2)
x = 0
y = 0
m = 0
for iy in range(s[0]):
    for ix in range(s[1]):
        if (z2[iy,ix]==1):
            x = x+ix
            y = y+iy
            m = m+1
xcm = x/m
ycm = y/m
plt.plot(xcm,ycm,'kx')
print(xcm,ycm)
plt.savefig("Fig136CenterofMass.png",dpi=120)
plt.show()






            


