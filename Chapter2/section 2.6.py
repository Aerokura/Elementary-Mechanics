# section 2.6 condition：throw a dice and go
# run with the code and then remove those sharps(i.e. #) and run it again
import matplotlib.pyplot as plt
import numpy as np
import math
import random

n = 1000
x = np.zeros(n, float)
for i in range(n-1):
    if random.randint(0, 5) + 1 <= 3:
        dx = -1
    else:
        dx = 1
    x[i+1] = x[i]+dx
    # if x[i+1] > 5:
    #     x[i+1] = 5
    # else:
    #     if x[i+1] < -5:
    #         x[i+1] = -5

plt.plot(x)
plt.xlabel('i')
plt.ylabel('x(i)')
# plt.ylim([-30, 30])
plt.xlim([0, 1000])
plt.show()