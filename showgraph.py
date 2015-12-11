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

    year_data = [0, 1, 2, 3, 4, 5]
    year_future = [5, 6]

    number_car = [[[28.1, 29.9, 31.8, 34.2, 35.6, 36.5],[36.5, 38.3]],\
                  [[0, 1.7, 1.8, 2.4, 1.3, 0.9],[0.9, 1.8]]]

    subplot = [211, 212]
    title = ['Show stock car and future stock car(2016).',\
             'Show increment of car and future increment of car(2016)']

    for i in range(2):
        graph_ = fig.add_subplot(subplot[i])
        graph_.set_title(title[i], fontsize = 12)
        graph_.set_ylabel('Total(Million)')
        if i == 1:
            graph_.set_xlabel('Year201X')
            
        if i == 0:
            number_car = [28.1, 29.9, 31.8, 34.2, 35.6, 36.5]

            plot_graph(year_data, number_car, graph_, 0, in_c, in_label,in_facecolor)

            car_future = [36.5, 38.3]

            plot_graph(year_future, car_future, graph_, 1, in_c, in_label,in_facecolor)

            leg = graph_.legend(loc='lower right')

        elif i == 1:
            increase_car = [0, 1.7, 1.8, 2.4, 1.3, 0.9]

            plot_graph(year_data, increase_car, graph_, 2, in_c, in_label,in_facecolor)

            increase_future = [0.9, 1.8]
            
            plot_graph(year_future, increase_future, graph_, 3, in_c, in_label,in_facecolor)
            
            leg = graph_.legend(loc='lower right')

    plt.show()

def plot_graph(year_data, number_car, graph_, nub, in_c, in_label,in_facecolor):
    graph_.plot(year_data, number_car, c=in_c[nub], label=in_label[nub], linewidth=2.5)
    for year_one, number_car in zip(year_data, number_car):
        plt.text(year_one, number_car, '%.1f' % number_car, ha='center', va= 'bottom',\
        bbox={'facecolor':in_facecolor[nub], 'alpha':0.5, 'pad':2.5})
"""        
#graph 1
    graph_1 = fig.add_subplot(211)
    graph_1.set_title('Show stock car and future stock car(2016).', fontsize = 12)
    graph_1.set_ylabel('Total(Million)')

    number_car = [28.1, 29.9, 31.8, 34.2, 35.6, 36.5]

    plot_graph(year_data, number_car, graph_1, 0, in_c, in_label,in_facecolor)

    car_future = [36.5, 38.3]

    plot_graph(year_future, car_future, graph_1, 1, in_c, in_label,in_facecolor)

    leg = graph_1.legend(loc='lower right')

#graph2
    graph_2 = fig.add_subplot(212)
    graph_2.set_title('Show increment of car and future increment of car(2016)', fontsize = 12)
    graph_2.set_xlabel('Year201X')
    graph_2.set_ylabel('Total(Million)')

    increase_car = [0, 1.7, 1.8, 2.4, 1.3, 0.9]

    plot_graph(year_data, increase_car, graph_2, 2, in_c, in_label,in_facecolor)

    increase_future = [0.9, 1.8]
    
    plot_graph(year_future, increase_future, graph_2, 3, in_c, in_label,in_facecolor)
    
    leg = graph_2.legend(loc='lower right')

    plt.show()
"""


make_graph()
