from typing import Dict, List, Optional, Set, Tuple
from .triats.base import OrganismTriats


class Organism:
    def __init__(self, x, y, dna, brain):
        self.is_alive = True
        self.x = x
        self.y = y
        self.age = 0
        self.dna = dna
        self.triats: Dict[str, "OrganismTriats"] = {}
        self.energy = self.dna.max_energy
        self.brain = brain
        print(f"NA START: {self.energy}")

    def decide(self, obs):
        inputs = [self.energy/self.dna.max_energy] + obs
        return self.brain.decide(inputs)


    def lose_energy(self, amount):
        self.energy -= amount
        if self.energy <= 0:
            self.is_alive = False


    def add_energy(self, amount) -> None:
        self.energy += amount
        if self.energy >= self.dna.max_energy:
            self.energy = self.dna.max_energy
        if self.energy <= 0:
            self.is_alive = False
        print(f"COS ODJEBAL: {self.energy}")


    # ------------------triats ----------------------
    def add_triat(self, name, triat):
        pass

    def get_triat(self, name):
        pass

    def has_triat(self, name):
        pass

    def remove_triat(self, name):
        pass


        #print("EAT")


    # def get_vision(self, grid):
    #     # Sprawdzamy tylko 4 pola
    #     dirs = [
    #         (0, -1),  # Góra
    #         (1, 0),   # Prawo
    #         (0, 1),   # Dół
    #         (-1, 0)   # Lewo
    #     ]
        
    #     vision = []
    #     for dx, dy in dirs:
    #         tx, ty = self.x + dx, self.y + dy
    #         if not (0 <= tx < WIDTH and 0 <= ty < HEIGHT):
    #             vision.append(-1)  
    #         else:
    #             vision.append(grid[tx][ty])

    #     return vision


class DNA:
    def __init__(self, max_energy):
        self.max_energy = max_energy