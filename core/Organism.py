import random
from .config import EMPTY, FOOD, ORGANISM, MOVE_COST, MAX_ENERGY, WIDTH, HEIGHT
from .brain import Brain

move_cost = 5

class Organism:
    def __init__(self, x, y, dna, brain):
        self.is_alive = True
        self.x = x
        self.y = y
        self.age = 0
        self.dna = dna
        self.energy = self.dna.max_energy
        self.vision = self.dna.vision

        self.food_eaten = 0

        if brain is None:
            #print("Nowy mozg")
            self.brain = Brain()
        else:
            #print("Zmodyfikowany mozg")
            self.brain = brain

    def choose_direction(self, grid):
        vision = self.get_vision(grid)
        energy = self.energy / MAX_ENERGY
        inputs = [energy] + vision
        return self.brain.decide(inputs)
        # dx = random.choice([1, -1, 0])
        # dy = random.choice([1, -1, 0])
        # return dx, dy

    def lose_energy(self, amount):
        self.energy -= amount
        if self.energy <= 0:
            self.is_alive = False
            #print(f"DEAD at age {self.age}")

    def add_energy(self, amount):
        self.energy += amount
        if self.energy >= 100:
            self.energy = 100
        self.food_eaten += 1
        #print("EAT")

    def get_vision(self, grid):
        # Sprawdzamy tylko 4 pola
        dirs = [
            (0, -1),  # Góra
            (1, 0),   # Prawo
            (0, 1),   # Dół
            (-1, 0)   # Lewo
        ]
        
        vision = []
        for dx, dy in dirs:
            tx, ty = self.x + dx, self.y + dy
            if not (0 <= tx < WIDTH and 0 <= ty < HEIGHT):
                vision.append(-1)  
            else:
                vision.append(grid[tx][ty])

        return vision
        # vision = []
        # for dy in range(-2, 3):
        #     for dx in range(-2, 3):
        #         if dx == 0 and dy == 0:
        #             continue
        #         tx, ty = self.x + dx, self.y + dy
        #         if not (0 <= tx < WIDTH and 0 <= ty < HEIGHT):
        #             vision.append(-1)
        #         else:
        #             target = grid[tx][ty]
        #             vision.append(target)

        # return vision

class DNA:
    def __init__(self, max_energy, vision):
        self.max_energy = max_energy
        self.vision = vision