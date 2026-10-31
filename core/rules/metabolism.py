from .base import WorldRule
from ..config import ENERGY_LOSS_ON_TICK

class MetabolismRule(WorldRule):
    name = "metabolism"

    def on_organism_tick(self, world, organism) -> None:
        organism.lose_energy(ENERGY_LOSS_ON_TICK)
        print("ENERGY LOSS")