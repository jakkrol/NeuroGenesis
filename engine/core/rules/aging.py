from .base import WorldRule
from ..config import MAX_AGE

class AgingRule(WorldRule):
    name = "aging"

    def on_organism_tick(self, world, organism) -> None:
        if organism.age > MAX_AGE:
            world.kill(organism)
            print(f"DEAD BY AGE {organism.age}")