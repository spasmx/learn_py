import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set a name for the graph and each of the axes
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of value', fontsize=14)

# Set the font size for signatures on the markup
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each of the axes
ax.axis([0, 1100, 0, 1100000])

plt.show()
#plt.savefig('squares_plot.png', bbox_inches='tight')
