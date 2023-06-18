import matplotlib.pyplot as plt

from random_walk import RandomWalk


# Creating the new walk until program in active
while True:
    # Create random walk
    rw = RandomWalk(50000)
    rw.fill_walk()
    # Plot the random walk points on the graph
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds, edgecolors='none', s=1)
    # Hide axis
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # Separate the first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    plt.show()

    keep_running = input('Create the new walk? [y/n]: ')
    if keep_running == 'n':
        break


