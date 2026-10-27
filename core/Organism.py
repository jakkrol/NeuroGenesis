import random

class Organism:
    def __init__(self, x, y, dna):
        self.is_alive = True
        self.x = x
        self.y = y
        self.dna = dna
        self.energy = self.dna.max_energy
        self.vision = self.dna.vision

    def choose_direction(self):
        dx = random.choice([1, -1, 0])
        dy = random.choice([1, -1, 0])
        return dx, dy
        

class DNA:
    def __init__(self, max_energy, vision):
        self.max_energy = max_energy
        self.vision = vision