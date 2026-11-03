import random
from .base import BaseTrainer

class EvolutionTrainer(BaseTrainer):
    def __init__(self, world, brain_factory, population_size=25):
        super().__init__(world, brain_factory, population_size)
        # self.world.on("ate", self.on_organism_ate)
        # self.world.on("all_dead", self.on_all_organisms_dead)
        self.graveyard = []  
        self.collectivly_eaten = 0
        
    def step(self):
        self.world.step()

    def on_organism_died(self, organism):
        #print(f"Organism {organism} died at age {organism.age} with energy {organism.energy}.")
        self.graveyard.append(organism)  

    def on_organism_ate(self, organism, cell, energy):
        self.collectivly_eaten += 1
        pass

    def on_all_organisms_dead(self):
        print("All organisms are dead.")
        print(f"Collectivly eaten: {self.collectivly_eaten}")
        self.collectivly_eaten = 0
        ## Here the organisms should be evolved and new generation created
        self.graveyard.sort(key=lambda org: org.age, reverse=True)
        bests_count = max(2, int(self.population_size * 0.2))
        bests = self.graveyard[:bests_count]

        self.world.reset()

        for parent in bests:
            child = parent.brain.clone()
            self.world.spawn_organism(child)

        while len(self.world.organisms) < self.population_size:
            parent = random.choice(bests)
            child_brain = parent.brain.mutate()
            self.world.spawn_organism(child_brain)

        self.graveyard.clear()

    