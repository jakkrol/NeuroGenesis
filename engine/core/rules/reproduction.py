from .base import WorldRule
from ..triats.gender import GenderTrait
# Tutaj też kin trait bedzie potrzebny
from ..config import ORGANISM, DIRECTIONS

class ReproductionRule(WorldRule):
    name = "reproduction"
    additional_inputs = len(DIRECTIONS)

    def __init__(self):
        self.required_traits = {"gender": GenderTrait}
        print("Dodano rep rule")

    def on_blocked(self, world, organism, x, y, content):
        if content == ORGANISM:
            other_org = world.org_positions.get((x, y))
            print(f"Value of oranism gender: {organism.get_trait("gender")} and otehr org: {other_org.get_trait("gender")}")
                

    def get_tile_info(self, world, x, y, content):
        return 0