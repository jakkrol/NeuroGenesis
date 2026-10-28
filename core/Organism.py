import random

from .brain import Brain

move_cost = 5

class Organism:
    def __init__(self, x, y, dna):
        self.is_alive = True
        self.x = x
        self.y = y
        self.dna = dna
        self.energy = self.dna.max_energy
        self.vision = self.dna.vision
        self.brain = Brain()

    def choose_direction(self):
        return self.brain.decide()
        # dx = random.choice([1, -1, 0])
        # dy = random.choice([1, -1, 0])
        # return dx, dy

    def lose_energy(self, amount):
        self.energy -= amount
        if self.energy <= 0:
            self.is_alive = False
            print("DEAD")

    def add_energy(self, amount):
        self.energy += amount
        if self.energy >= 100:
            self.energy = 100
        print("EAT")

class DNA:
    def __init__(self, max_energy, vision):
        self.max_energy = max_energy
        self.vision = vision