from .base import BaseTrainer

class EvolutionTrainer(BaseTrainer):
    def __init__(self, world, brain_factory, population_size=25):
        super().__init__(world, brain_factory, population_size)
        # self.world.on("ate", self.on_organism_ate)
        # self.world.on("all_dead", self.on_all_organisms_dead)

        
    def step(self):
        self.world.step()

    def on_organism_died(self, organism):
        print(f"Organism {organism} died at age {organism.age} with energy {organism.energy}.")
        # Here the statistics of a turn can be collected, for example array of ages of dead organisms for evolution selection

    def on_organism_ate(self, organism, cell, energy):
        pass

    def on_all_organisms_dead(self):
        print("All organisms are dead.")
        ## Here the organisms should be evolved and new generation created

        self.start()

    