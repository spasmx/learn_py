from random import choice


class RandomWalk:
    """The Class for generic random walk's"""

    def __init__(self, num_points=5000):
        """Initialize walk attributes"""
        self.num_points = num_points
        # All random walk's start with (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate of all points of the walk"""
        # Continue to take steps until the wandering reaches the required length
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            # Discard steps that do not advance anywhere
            if x_step == 0 and y_step == 0:
                continue
            # Calculate a new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    @staticmethod
    def get_step():
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4, 5])
        step = direction * distance
        return step



