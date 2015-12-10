import numpy as np
import matplotlib.pyplot as plt
x = [0,1,2,3,4,5]
y = [2.9,2.9,3.1,3.4,3.5,3.6]
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title('graph')
ax1.set_xlabel('year201X')
ax1.set_ylabel('value')
ax1.plot(x,y,c='b',label='stock car')
a = [0,1,2,3,4,5]
b = [1.7,1.7,1.8,2.4,1.3,0.9]
ax1.plot(a,b,c='r',label='diff car')
leg = ax1.legend(loc='upper left')
plt.show()
