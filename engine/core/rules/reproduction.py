from .base import WorldRule
from ..triats.gender import GenderTrait
from ..triats.kin import KinTrait
# Tutaj też kin trait bedzie potrzebny
from ..config import ORGANISM, DIRECTIONS

class ReproductionRule(WorldRule):
    name = "reproduction"
    priority = 100
    additional_inputs = len(DIRECTIONS)

    def __init__(self):
        self.required_traits = {"gender": GenderTrait, "kin": KinTrait}
        print("Dodano rep rule")

    def on_blocked(self, world, organism, x, y, content):
        if content == ORGANISM:
            other_org = world.org_positions.get((x, y))
            kin = organism.triats["kin"]
            is_family = (other_org.id in kin.parents) or (other_org.id in kin.children)

            if not is_family:
                print(f"Value of oranism gender: {organism.id, organism.get_trait("gender")} and other org: {other_org.id, other_org.get_trait("gender")}")
                return True

        return False

    def get_tile_info(self, world, x, y, content):
        #Tutaj musimy gender pobrać
        return 0