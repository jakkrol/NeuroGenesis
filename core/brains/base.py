class BaseBrain:
    def __init__(self, add_dims = 0):
        self.add_dims = add_dims

    def decide(self, inputs):
        #print(inputs)
        return 0