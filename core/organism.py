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
        #print(f"NA START: {self.energy}")


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


    # ------------------triats ----------------------
    def add_trait(self, name, trait):
        self.triats[name] = trait

    def get_trait(self, name):
        return self.triats[name].val

    def has_trait(self, name):
        pass

    def remove_trait(self, name):
        pass




class DNA:
    def __init__(self, max_energy):
        self.max_energy = max_energy