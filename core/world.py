import random

from .organism import Organism, DNA
from .brain import mutate
from .config import EMPTY, FOOD, ORGANISM, MOVE_COST, MAX_ENERGY, WIDTH, HEIGHT, FOOD_ON_MAP

class World:
    def __init__(self, width, height, num_organisms, init_food):
        self.width = width
        self.height = height
        self.organisms = []
        self.world_grid = self._empty_grid()

    def generate_world(self, init_food, num_oraganisms):
        for _ in range(init_food):
            self.spawn_single_food()
        for _ in range(num_oraganisms):
            self.spawn_organism()

    def _empty_grid(self):
        return [[EMPTY for _ in range(self.height)] for _ in range(self.width)]

    def reset(self):
        self.world_grid = self._empty_grid()
        self.organisms = []


    def spawn_single_food(self):
        while True:
            pos_x = random.randint(0, self.width - 1)
            pos_y = random.randint(0, self.height - 1)
            if self.world_grid[pos_x][pos_y] == EMPTY:
                break

        self.world_grid[pos_x][pos_y] = FOOD

    def spawn_organism(self, brain=None):
        while True:
            pos_x = random.randint(0, self.width - 1)
            pos_y = random.randint(0, self.height - 1)
            if self.world_grid[pos_x][pos_y] == EMPTY:
                break

        self.world_grid[pos_x][pos_y] = ORGANISM

        # Add new organism to array
        new_dna = DNA(100, 3)
        new_organism = Organism(pos_x, pos_y, new_dna, brain)
        self.organisms.append(new_organism)

    # Here the entire world state will be updated and prepared for redraw in sim window
    def update(self):
        for organism in self.organisms:
            if not organism.is_alive:
                continue

            organism.age += 1
            dx, dy = organism.choose_direction(self.world_grid)
            new_x = organism.x + dx
            new_y = organism.y + dy

            if 0 <= new_x < self.width and 0 <= new_y < self.height:
                target = self.world_grid[new_x][new_y]
                if target == EMPTY:
                    self.world_grid[organism.x][organism.y] = EMPTY
                    organism.x = new_x
                    organism.y = new_y
                    self.world_grid[organism.x][organism.y] = ORGANISM
                elif target == FOOD:
                    self.world_grid[organism.x][organism.y] = EMPTY
                    organism.x = new_x
                    organism.y = new_y
                    self.world_grid[organism.x][organism.y] = ORGANISM
                    organism.add_energy(20)
                    
            organism.lose_energy(2)
            if not organism.is_alive:
                self.world_grid[organism.x][organism.y] = EMPTY

        # Sprawdzamy, czy KTÓRYKOLWIEK organizm jeszcze żyje.
        any_alive = any(org.is_alive for org in self.organisms)
        if not any_alive:
            self.check_generation_end()






    def check_generation_end(self):
        alive = [o for o in self.organisms if o.is_alive]

        if len(alive) == 0:
            self.clear_world()
            for _ in range(FOOD_ON_MAP):
                self.spawn_single_food()
            print("Gen ended")
            # Tutaj trzeba zaimplemenować selekcje i mutacje
            ##########

            ### Fitness na głównie na podst. jedzenia
            #self.organisms.sort(key=lambda o: o.age, reverse=True)
            self.organisms.sort(key=lambda o: o.food_eaten, reverse=True)
            top = max(5, len(self.organisms)//10)
            top_parents = self.organisms[:top]
            print(f"Najlepszy stworek zjadł: {top_parents[0].food_eaten} jedzenia i przeżył {top_parents[0].age} tur.")
            self.organisms = []

            for _ in range(100):
                parent = random.choice(top_parents)
                child_brain = mutate(parent.brain)
                self.spawn_organism(child_brain)
            ##########
