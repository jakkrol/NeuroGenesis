from .base import OrganismTriats
import random

class GenderTrait(OrganismTriats):
    name = "sex"

    def __init__(self):
        self.val = random([-1, 1])