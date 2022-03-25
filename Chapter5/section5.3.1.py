#5.3.1 Example：Acceleration and Forces on a Lunar Lander
import numpy as np
import matplotlib.pyplot as plt
import math
[t,a] = np.loadtxt('Chapter5/data/reentry.txt',usecols=[0,1],unpack=True)
W = 49000.0 # N
m = 5000.0 # kg
D = W + m*a 
plt.plot(t,D)
plt.xlabel('t [s]')
plt.ylabel('D [N]')
plt.show()
selected = [x for x in D if x<1e6]
print(selected)
# find the smallest i where D(ti) is less than D
maxD= max(selected)
i = [x for x, y in list(enumerate(D)) if y ==maxD]
print(i)
ti = t[i]
print(ti)# ti = 5.4246 s. The air resistance force falls to 10^6 N after 5.42s