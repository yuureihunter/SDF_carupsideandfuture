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

    in_c = [['b', 'r'], ['g', '#FF8C00']]
    in_label = [['Stock car', 'Future stock car(2016)'], ['Diff car', 'Future diff car(2016)']]
    in_facecolor = [['#B0E0E6', '#FA8072'], ['#54FF9F', '#FF8C00']]

    year_data = [[0, 1, 2, 3, 4, 5], [5, 6]]

    number_car_data = [[[28.1, 29.9, 31.8, 34.2, 35.6, 36.5], [36.5, 38.3]]]
    find_dif(number_car_data)

    subplot = [211, 212]
    title = ['Show stock car and future stock car(2016).',\
             'Show increment of car and future increment of car(2016)']

    for i in range(2):
        graph_ = fig.add_subplot(subplot[i])
        graph_.set_title(title[i], fontsize = 12)
        graph_.set_ylabel('Total(Million)')
        if i == 1:
            graph_.set_xlabel('Year201X')

        for j in range(2):
            number_car = number_car_data[i][j]
            plot_graph(year_data[j], number_car, graph_, i, j, in_c, in_label, in_facecolor)
            leg = graph_.legend(loc='lower right')

    plt.show()

def find_dif(number_car_data):
    """return different of number car each years"""
    ans = [[0]]
    for j in range(len(number_car_data[0])):
        data = number_car_data[0][j]
        for i in range(1, len(data)):
            dif = "%.2f" % (data[i] - data[i-1])
            ans[j].append(float(dif))
        if j == len(data) - 1:
            return number_car_data.append(ans) 
        ans.append([ans[j][-1]])

def plot_graph(year_data, number_car, graph_, i, j, in_c, in_label, in_facecolor):
  """plot point on this graph"""
  graph_.plot(year_data, number_car, c=in_c[i][j], label=in_label[i][j], linewidth=2.5)
  for year_one, number_car in zip(year_data, number_car):
      plt.text(year_one, number_car, '%.1f' % number_car, ha='center', va= 'bottom',\
               bbox={'facecolor':in_facecolor[i][j], 'alpha':0.5, 'pad':2.5})

make_graph()
