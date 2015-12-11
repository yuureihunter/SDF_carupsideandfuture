"""Graph of stock car in september 2010 - 2015(Thailand)"""
import matplotlib.pyplot as plt
def make_graph():
    """Make Line Graph in two box, first box show data of stock car(Show in Blue Line) and show data in future stock car(Show in Red Line)
       ,and second box show data of diff of car (Show in Line Green) and show data in future diff of car (Show in Red line)."""
    fig = plt.figure()
    plt.style.use('bmh') #ใส่พื้นหลัง
    fig.suptitle('Graph of stock car in september 2010 - 2015(Thailand)', fontsize=18, fontweight='bold')
    graph_1 = fig.add_subplot(211)
    graph_1.set_title('Show stock car and future stock car(2016).', fontsize = 12)
    graph_1.set_ylabel('Total(Million)') #ล้าน
    
    year_one = [0, 1, 2, 3, 4, 5]
    number_car = [28.1, 29.9, 31.8, 34.2, 35.6, 36.5]
    graph_1.plot(year_one, number_car, c='b', label='Stock car', linewidth=2.5)
    for year_one, number_car in zip(year_one, number_car):
        plt.text(year_one, number_car, '%.2f' % number_car, ha='center', va= 'bottom',\
        bbox={'facecolor':'#B0E0E6', 'alpha':0.5, 'pad':2.5}) #สีกล่องข้อความตามจุด
    year_future_one = [5, 6]
    car_future = [36.5, 38.3] #ค่าสุดท้ายคิดเรียบร้อยแล้ว
    graph_1.plot(year_future_one, car_future, c='r',label='Future stock car(2016)', linewidth=2.5)
    for year_one, number_car in zip(year_future_one, car_future):
        plt.text(year_one, number_car, '%.2f' % number_car, ha='center', va= 'bottom',\
        bbox={'facecolor':'#FA8072', 'alpha':0.5, 'pad':2.5})
    leg = graph_1.legend(loc='lower right') #สิ้นสุดโค้ดกราฟแสดงจำนวนรถสะสม

    graph_2 = fig.add_subplot(212)
    graph_2.set_title('Show increment of car and future increment of car(2016)', fontsize = 12)
    graph_2.set_xlabel('Year201X')
    graph_2.set_ylabel('Total(Million)') #ล้าน

    year_two = [0, 1, 2, 3, 4, 5]
    increase_car = [0, 1.7, 1.8, 2.4, 1.3, 0.9]
    graph_2.plot(year_two, increase_car, c='g', label='Diff car', linewidth=2.5)
    for year_one, number_car in zip(year_two, increase_car):
        plt.text(year_one, number_car, '%.1f' % number_car, ha='center', va= 'bottom',\
        bbox={'facecolor':'#54FF9F', 'alpha':0.4, 'pad':2.5})
    year_future_two = [5, 6]
    increase_future = [0.9, 1.8] #ค่าสุดท้ายคิดเรียบร้อยแล้ว
    graph_2.plot(year_future_two, increase_future, c='r', label='Future diff car(2016)', linewidth=2.5)
    for year_one, number_car in zip(year_future_two, increase_future):
        plt.text(year_one, number_car, '%.1f' % number_car, ha='center', va= 'bottom',\
        bbox={'facecolor':'#FF8C00', 'alpha':0.5, 'pad':2.5})
    leg = graph_2.legend(loc='lower right') #สิ้นสุดโค้ดกราฟแสดงจำนวนการเพิ่มขึ้นของรถ
    plt.show()
make_graph()

#ใครว่างฝากทดสอบโค้ดด้วยจ้า#

