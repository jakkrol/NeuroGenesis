import random
from .base import BaseBrain
from ..config import DIRECTIONS

class RandomBrain(BaseBrain):
    def decide(self, inputs):
        return random.randrange(len(DIRECTIONS))