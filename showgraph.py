"""Graph of stock car in september 2010 - 2015(Thailand)"""
import numpy as np
import matplotlib.pyplot as plt
def make_graph():
    """Make Line Graph in two box, first box show data of stock car(Show in Blue Line) and show data in future stock car(Show in Red Line)
       ,and second box show data of diff of car (Show in Line Green) and show data in future diff of car (Show in Red line)."""
    fig = plt.figure()
    plt.style.use('bmh') #ใส่พื้นหลัง
    fig.suptitle('Graph of stock car in september 2010 - 2015(Thailand)', fontsize=18, fontweight='bold')
    ax1 = fig.add_subplot(211)
    ax1.set_title('Show stock car and future stock car(2016).', fontsize = 12)
    ax1.set_ylabel('Total(Million)') #ล้าน
    
    year_one = [0, 1, 2, 3, 4, 5]
    number_car = [28.1, 29.9, 31.8, 34.2, 35.6, 36.5]
    ax1.plot(year_one, number_car, c='b', label='Stock car', linewidth=2.5)
    for year_one, number_car in zip(year_one, number_car):
        plt.text(year_one, number_car, '%.2f' % number_car, ha='center', va= 'bottom',\
        bbox={'facecolor':'#B0E0E6', 'alpha':0.5, 'pad':2.5}) #สีกล่องข้อความตามจุด
    w = [5, 6]
    z = [36.5, 38.3] #ค่าสุดท้ายคิดเรียบร้อยแล้ว
    ax1.plot(w, z, c='r',label='Future stock car(2016)', linewidth=2.5)
    for year_one, number_car in zip(w, z):
        plt.text(year_one, number_car, '%.2f' % number_car, ha='center', va= 'bottom',\
        bbox={'facecolor':'#FA8072', 'alpha':0.5, 'pad':2.5})
    leg = ax1.legend(loc='lower right') #สิ้นสุดโค้ดกราฟแสดงจำนวนรถสะสม

    ax2 = fig.add_subplot(212)
    ax2.set_title('Show increment of car and future increment of car(2016)', fontsize = 12)
    ax2.set_xlabel('Year201X')
    ax2.set_ylabel('Total(Million)') #ล้าน

    a = [0, 1, 2, 3, 4, 5]
    b = [0, 1.7, 1.8, 2.4, 1.3, 0.9]
    ax2.plot(a, b ,c='g', label='Diff car', linewidth=2.5)
    for year_one, number_car in zip(a, b):
        plt.text(year_one, number_car, '%.1f' % number_car, ha='center', va= 'bottom',\
        bbox={'facecolor':'#54FF9F', 'alpha':0.4, 'pad':2.5})
    g = [5, 6]
    h = [0.9, 1.8] #ค่าสุดท้ายคิดเรียบร้อยแล้ว
    ax2.plot(g, h, c='r', label='Future diff car(2016)', linewidth=2.5)
    for year_one, number_car in zip(g, h):
        plt.text(year_one, number_car, '%.1f' % number_car, ha='center', va= 'bottom',\
        bbox={'facecolor':'#FF8C00', 'alpha':0.5, 'pad':2.5})
    leg = ax2.legend(loc='lower right') #สิ้นสุดโค้ดกราฟแสดงจำนวนการเพิ่มขึ้นของรถ
    plt.show()
make_graph()
#test edit by sea#
#test edit by poogun#
#ใครว่างฝากทดสอบโค้ดด้วยจ้า#
