class BaseTrainer:
    def __init__(self, world, brain_factory, population_size=25):
        self.world = world
        self.brain_factory = brain_factory
        self.population_size = population_size

        self.additional_triats = {} # TUTAJ BEDA TRAITS DODANE DO SYMULACJI


        self.world.on("ate", self.on_organism_ate)
        self.world.on("all_dead", self.on_all_organisms_dead)
        self.world.on("organism_died", self.on_organism_died)

        self.additional_dims = self.world.calc_additional_dims()

    def start(self):
        self.world.reset()
        for _ in range(self.population_size):
            org = self.world.spawn_organism(self.brain_factory(add_dims=self.additional_dims))

            # for name, trait in self.additional_triats:
            #     org.add_trait()

    def step(self):
        self.world.step()

