#page 410 13.2.4 Center of mass from image analysis
#复现书上例题“13.2.4 Example: Center of Mass from Image Analysis”的程序，处理图片可以直接从书上电子版截取，不同同学不需要相同，讨论滤镜选择的方式对形心判断的影响。
import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.image as mpimg
Q = mpimg.imread('./blank.png')# RGB 0--255
#print(Q.shape)
#print(Q[0:2,0:2,0])
z = mpimg.imread('./ballimage02cut.png')# RGB 0--255
#print(type(z))
#print(z.shape)
plt.subplot(3,1,1)
plt.imshow(z)
#plt.axis('equal')
z2 = (z[:,:,0]+z[:,:,1]+z[:,:,2]*10)<1.5#去掉蓝光，剔除背景
print(type(z2))
print(z2.shape)
plt.subplot(3,1,2)
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
z3 = np.zeros((s[0],s[1]))
for ix in range(s[0]):
    for iy in range(s[1]):
        if (1.1*z[ix,iy,0]+z[ix,iy,2]+0.7*z[ix,iy,1]>0.8):
            z3[ix,iy] = 1
z3 = np.array(z3)
plt.subplot(3,1,3)
plt.imshow(z3)
s3 = np.shape(z3)
print(s3)
x3 = 0
y3 = 0
m3 = 0
for iy in range(s3[0]):
    for ix in range(s3[1]):
        if (z3[iy,ix]==1):
            x3 = x3+ix
            y3 = y3+iy
            m = m+1
xcm3 = x3/m
ycm3 = y3/m
plt.plot(xcm3,ycm3,'kx')
print(xcm3,ycm3)
plt.savefig("Fig136CenterofMassnoidea.png",dpi=120)
plt.show()






            


