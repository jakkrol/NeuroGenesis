class BaseTrainer:
    def __init__(self, world):
        self.world = world
        self.world.on("ate", self.on_organism_ate)

    def step(self):
        self.world.step()

    def on_organism_ate(self, organism, cell, energy):
        print(f"Organism {organism} ate cell {cell} and gained {energy} energy.")