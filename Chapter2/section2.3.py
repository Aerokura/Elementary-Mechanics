from pylab import *
import matplotlib.pyplot as plt
import numpy as np
m = np.array([1.0,2.0,4.0,6.0,9.0,11.0]) 
V = np.array([0.13,0.26,0.50,0.77,1.15,1.36])
print(m[0])
plt.plot(m,V,'o')
plt.xlabel('m (kg)')
plt.ylabel('V (l)')

for value in np.array([1.0,2.0,4.0,6.0,9.0,11.0]):
    print(type(value))
plt.show()