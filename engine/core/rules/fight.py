from ..config import ORGANISM, DIRECTIONS
from .base import WorldRule

class FightRule(WorldRule):
    name="fight"
    additional_inputs = len(DIRECTIONS)

    def on_blocked(self, world, organism, x, y, content):
        if content == ORGANISM:
            other_org = world.org_positions.get((x, y))
            if other_org is not None:
                # For now it will be simple: the one with more energy wins
                if organism.energy > other_org.energy:
                    world.kill(other_org)
                    organism.add_energy(200) ## For now, it gets full energy, will be adjusted later
                elif organism.energy < other_org.energy:
                    world.kill(organism)
                    other_org.add_energy(200) ## For now, it gets full energy, will be adjusted later
                print(f"Fight between {organism} and {other_org}. Winner: {organism if organism.energy > other_org.energy else other_org}")


    def get_tile_info(self, world, x, y, content):
        if content == ORGANISM:
            org = world.org_positions.get((x, y))
            return org.energy / 100
        else:
            return 0
