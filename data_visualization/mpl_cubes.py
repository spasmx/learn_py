import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
cubes = [1, 8, 27, 64, 125]

plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(input_values, cubes, linewidth=3)

# Set a name for the graph and each of the axes
ax.set_title('Cube Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube of Value', fontsize=14)

# Set the font size for signatures on the markup
ax.tick_params(axis='both', labelsize=14)

plt.show()