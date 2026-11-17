from .base import OrganismTriats

class KinTrait(OrganismTriats):
    name = "kin"

    def __init__(self, parents=None):
        self.parents = set(parents) if parents else set()
        self.children = set()
        print("Wywołano kin triat")