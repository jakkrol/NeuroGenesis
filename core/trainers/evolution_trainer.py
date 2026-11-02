from .base import BaseTrainer

class EvolutionTrainer(BaseTrainer):
    def __init__(self, world):
        self.world = world
        self.world.on("ate", self.on_organism_ate)
        self.world.on("all_dead", self.on_all_organisms_dead)

    def step(self):
        self.world.step()

 

    def on_organism_ate(self, organism, cell, energy):
        pass

    def on_all_organisms_dead(self):
        print("All organisms are dead.")

    