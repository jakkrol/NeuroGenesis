class BaseTrainer:
    def __init__(self, world):
        self.world = world

    def step(self):
        self.world.step()