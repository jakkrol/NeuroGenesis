from core.config import WIDTH, HEIGHT
from core.world import World
from core.rules.food import FoodRule
from core.rules.metabolism import MetabolismRule
from core.rules.aging import AgingRule
from ui.sim_window import SimWindow
from core.brains.base import BaseBrain 
from core.brains.random import RandomBrain 

NUM_ORGANISMS = 1

if __name__ == "__main__":
    world = World(WIDTH, HEIGHT)

    food = FoodRule()
    world.add_rule(food)
    food.spawn(world, 300)

    poison = FoodRule(2, -10)
    world.add_rule(poison)
    poison.spawn(world, 300)

    #world.add_rule(MetabolismRule())
    world.add_rule(AgingRule())

    for _ in range(NUM_ORGANISMS):
        world.spawn_organism(RandomBrain())


    SimWindow(world).run()