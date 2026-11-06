from .base import OrganismTriats
import random

class GenderTrait(OrganismTriats):
    name = "gender"

    def __init__(self):
        self.val = random.choice([-1, 1])
        print("Wywolano gender trait")

    def clone_for_child(self):
        return GenderTrait()