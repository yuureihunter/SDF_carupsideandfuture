import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title('graph')
ax1.set_xlabel('year201X')
ax1.set_ylabel('value')
x = [0,1,2,3,4,5]
y = [28.1,29.9,31.8,34.2,35.6,36.5]
ax1.plot(x,y,c='b',label='stock car')
for x,y in zip(x,y):
    plt.text(x, y, '%.2f' % y, ha='center', va= 'bottom',\
    bbox={'facecolor':'#B0E0E6', 'alpha':0.5, 'pad':2.5}) #สีกล่องข้อความตามจุด
w = [5,6]
z = [36.5,37.0] #ค่าสุดท้ายยังไมใช่ค่าจริง
ax1.plot(w,z,c='r',label='future stock car')
for x,y in zip(w,z):
    plt.text(x, y, '%.2f' % y, ha='center', va= 'bottom',\
    bbox={'facecolor':'#FA8072', 'alpha':0.5, 'pad':2.5})

a = [0,1,2,3,4,5]
b = [0,1.7,1.8,2.4,1.3,0.9]
ax1.plot(a,b,c='g',label='diff car')
for x,y in zip(a,b):
    plt.text(x, y, '%.1f' % y, ha='center', va= 'bottom',\
    bbox={'facecolor':'#54FF9F', 'alpha':0.5, 'pad':2.5})
g = [5,6]
h = [0.9,1.5] #ค่าสุดท้ายยังไม่ใช่ค่าจริง
ax1.plot(g,h,c='r',label='future diff car')
for x,y in zip(g,h):
    plt.text(x, y, '%.1f' % y, ha='center', va= 'bottom',\
    bbox={'facecolor':'#FF8C00', 'alpha':0.5, 'pad':2.5})

leg = ax1.legend(loc='center right')
print("end")
print("test")
