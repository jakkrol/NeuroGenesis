from ..config import FOOD, FOOD_ENERGY_GAIN
from .base import WorldRule

class FoodRule(WorldRule):
    def __init__(self, cell_code: int = FOOD, energy: float = FOOD_ENERGY_GAIN, name: str = None):
        self.cell_code = cell_code
        self.energy = energy
        self.name = name or f"food_{cell_code}"

    def on_attach(self, world):
        world.passable.add(self.cell_code)

    def on_detach(self, world):
        world.passable.discard(self.cell_code)
        world.clear_cells(self.cell_code)

    def on_enter(self, world, organism, x, y, previous):
        if previous == self.cell_code:
            organism.add_energy(self.energy)
            #world.emit("ate", organism, cell=self.cell_code, energy=self.energy)

    def spawn(self, world, count: int) -> int:
        return world.scatter(self.cell_code, count)