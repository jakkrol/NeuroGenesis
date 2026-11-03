from core.config import WIDTH, HEIGHT
from core.world import World
from core.rules.food import FoodRule
from core.rules.metabolism import MetabolismRule
from core.rules.fight import FightRule
from core.rules.aging import AgingRule
from ui.sim_window import SimWindow
from core.brains.base import BaseBrain 
from core.brains.random import RandomBrain
from core.brains.mlp import MLP
from core.trainers.base import BaseTrainer
from core.trainers.evolution_trainer import EvolutionTrainer

NUM_ORGANISMS = 100

if __name__ == "__main__":
    world = World(WIDTH, HEIGHT)

    world.add_rule(FoodRule(count=600))
    #world.add_rule(FoodRule(2, -10, 300))
    world.add_rule(MetabolismRule())
    #world.add_rule(AgingRule())
    #world.add_rule(FightRule())

    # world.reset()

    # for _ in range(NUM_ORGANISMS):
    #     world.spawn_organism(MLP())


    trainer = EvolutionTrainer(world, MLP, population_size=NUM_ORGANISMS)
    trainer.start()
    SimWindow(trainer).run()