import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
fig.suptitle('Graph of stock car in september 2010 - 2015', fontsize=18, fontweight='bold')
ax1 = fig.add_subplot(211)
ax1.set_title('show stock car and future stock car',fontsize = 12)
ax1.set_ylabel('value(millon)') #ล้าน
x = [0,1,2,3,4,5]
y = [2.81,29.9,31.8,34.2,35.6,36.5]
ax1.plot(x,y,c='b',label='stock car',linewidth=2.5)
for x,y in zip(x,y):
    plt.text(x, y, '%.2f' % y, ha='center', va= 'bottom',\
    bbox={'facecolor':'#B0E0E6', 'alpha':0.5, 'pad':2.5}) #สีกล่องข้อความตามจุด
w = [5,6]
z = [36.5,37.0] #ค่าสุดท้ายยังไมใช่ค่าจริง
ax1.plot(w,z,c='r',label='future stock car',linewidth=2.5)
for x,y in zip(w,z):
    plt.text(x, y, '%.2f' % y, ha='center', va= 'bottom',\
    bbox={'facecolor':'#FA8072', 'alpha':0.5, 'pad':2.5})
leg = ax1.legend(loc='lower right') #สิ้นสุดโค้ดกราฟแสดงจำนวนรถสะสม

ax2 = fig.add_subplot(212)
ax2.set_title('show diff of car and future diff of car',fontsize = 12)
ax2.set_xlabel('year201X')
ax2.set_ylabel('value(million)') #ล้าน

a = [0,1,2,3,4,5]
b = [0,1.7,1.8,2.4,1.3,0.9]
ax2.plot(a,b,c='g',label='diff car',linewidth=2.5)
for x,y in zip(a,b):
    plt.text(x, y, '%.1f' % y, ha='center', va= 'bottom',\
    bbox={'facecolor':'#54FF9F', 'alpha':0.4, 'pad':2.5})
g = [5,6]
h = [0.9,1.5] #ค่าสุดท้ายยังไม่ใช่ค่าจริง
ax2.plot(g,h,c='r',label='future diff car',linewidth=2.5)
for x,y in zip(g,h):
    plt.text(x, y, '%.1f' % y, ha='center', va= 'bottom',\
    bbox={'facecolor':'#FF8C00', 'alpha':0.5, 'pad':2.5})
leg = ax2.legend(loc='upper right') #สิ้นสุดโค้ดกราฟแสดงจำนวนการเพิ่มขึ้นของรถ
plt.show()
#test edit by sea#
#test edit by poogun#
#ใครว่างฝากทดสอบโค้ดด้วยจ้า#
