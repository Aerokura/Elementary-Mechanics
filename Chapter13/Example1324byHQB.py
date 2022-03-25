# Edited by Dr.Mengying Zhang  zhangmengyingkd@163.com
# This version is for Example 13.2.4. The script is done by Year 1 student Qibin Hu. 
# Updated on 25/03/2022
import matplotlib.pyplot as plt
import matplotlib.image as mp#读图的库
from numpy import *
tu=mp.imread('2.jpg')/255#.jpg格式的图没有进行归一处理，故要先除以255进行归一
#如果是png格式的图就不用进行归一处理
#imread读出来的图是以数组形式进行储存的
x=0
y=0
m=0
tu1=(tu[:,:,0]+tu[:,:,1]+tu[:,:,2])<1.5#见教材
s=shape(tu1)

plt.imshow(tu1)#, cmap="Greens")# Greens代表的是绿色隔窗，相当于主体是绿色
#图片中进行了布尔判断为True的点会被搞成绿色
for iy in range(s[0]):
    for ix in range(s[1]):
        if (tu1[iy,ix]==1):
            x=x+ix
            y=y+iy
            m+=1
xc=x/m
yc=y/m
plt.plot(xc,yc,'rx')
print((xc,yc))
plt.show()

