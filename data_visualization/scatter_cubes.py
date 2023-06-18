import matplotlib.pyplot as plt

x_values = range(1, 501)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

# Set a name for the graph and each of the axes
ax.set_title('Cube Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube of value', fontsize=14)

# Set the font size for signatures on the markup
ax.tick_params(axis='both', which='major', labelsize=14)

ax.ticklabel_format(axis='both', style='plain')

# Set the range for each of the axes
ax.axis([0, 510, 0, 132651000])

plt.show()
