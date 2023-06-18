from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die1 = Die()
die2 = Die()

results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

frequenсies= []
max_result = die1.num_sides + die2.num_sides
for val in range(2, max_result + 1):
    frequency = results.count(val)
    frequenсies.append(frequency)

# Visualize result
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequenсies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 dies 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')


