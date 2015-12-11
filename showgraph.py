"""Graph of stock car in september 2010 - 2015(Thailand)"""
import matplotlib.pyplot as plt

fig = plt.figure()
plt.style.use('ggplot')
fig.suptitle('Graph of stock car in september 2010 - 2015(Thailand) V.2',\
             fontsize=18, fontweight='bold')



def make_graph():
    """Make Line Graph in two box, first box show data of stock car
(Show in Blue Line) and show data in future stock car(Show in Red Line)
,and second box show data of diff of car (Show in Line Green) and show
data in future diff of car (Show in Red line)."""

    in_c = ['b', 'r', 'g', '#FF8C00']
    in_label = ['Stock car', 'Future stock car(2016)', 'Diff car', 'Future diff car(2016)']
    in_facecolor = ['#B0E0E6', '#FA8072', '#54FF9F', '#FF8C00']
    
#graph 1

    year_data = [0, 1, 2, 3, 4, 5]
    number_car = [28.1, 29.9, 31.8, 34.2, 35.6, 36.5]

    graphone(year_data,number_car, 0, in_c, in_label,in_facecolor)

#graph2

    year_two = [0, 1, 2, 3, 4, 5]
    increase_car = [0, 1.7, 1.8, 2.4, 1.3, 0.9]

    graphtwo(year_two, increase_car, 2, in_c, in_label,in_facecolor)

    plt.show()

def plot_graph(year_data, number_car, graph_, nub, in_c, in_label,in_facecolor):
    graph_.plot(year_data, number_car, c=in_c[nub], label=in_label[nub], linewidth=2.5)
    for year_one, number_car in zip(year_data, number_car):
        plt.text(year_one, number_car, '%.1f' % number_car, ha='center', va= 'bottom',\
        bbox={'facecolor':in_facecolor[nub], 'alpha':0.5, 'pad':2.5}) 

def graphone(year_one, number_car, nub, in_c, in_label,in_facecolor):
    graph_1 = fig.add_subplot(211)
    graph_1.set_title('Show stock car and future stock car(2016).', fontsize = 12)
    graph_1.set_ylabel('Total(Million)')
    plot_graph(year_one, number_car, graph_1, 0, in_c, in_label,in_facecolor)
    year_future_one = [5, 6]
    car_future = [36.5, 38.3]
    plot_graph(year_future_one, car_future, graph_1, 1, in_c, in_label,in_facecolor)
    leg = graph_1.legend(loc='lower right')

def graphtwo(year_two, increase_car, nub, in_c, in_label,in_facecolor):
    graph_2 = fig.add_subplot(212)
    graph_2.set_title('Show increment of car and future increment of car(2016)', fontsize = 12)
    graph_2.set_xlabel('Year201X')
    graph_2.set_ylabel('Total(Million)')
    plot_graph(year_two, increase_car, graph_2, 2, in_c, in_label,in_facecolor)
    year_future_two = [5, 6]
    increase_future = [0.9, 1.8]
    plot_graph(year_future_two, increase_future, graph_2, 3, in_c, in_label,in_facecolor)
    leg = graph_2.legend(loc='lower right')

make_graph()
