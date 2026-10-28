import random

class Brain:
    def __init__(self):
        pass

    def decide(self, inputs):
        dx = random.choice([1, -1, 0])
        dy = random.choice([1, -1, 0])
        return dx, dy