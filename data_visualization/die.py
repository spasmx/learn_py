from random import randint


class Die:
    """A class represents one cube"""
    def __init__(self, num_sides = 6):
        """Define a cube with six faces"""
        self.num_sides = num_sides

    def roll(self):
        """Return random number from 1 to 6"""
        return randint(1, self.num_sides)
