import random

from .organism import Organism, DNA

EMPTY = 0
FOOD = 1
ORGANISM = 9

class World:
    def __init__(self, width, height, num_organisms, init_food):
        self.width = width
        self.height = height
        self.organisms = []
        self.world_grid = [[EMPTY for _ in range(height)] for _ in range(width)]
        self.generate_world(init_food, num_organisms)

    def generate_world(self, init_food, num_oraganisms):
        for _ in range(init_food):
            self.spawn_single_food()
        for _ in range(num_oraganisms):
            self.spawn_organism()


    def spawn_single_food(self):
        while True:
            pos_x = random.randint(0, self.width - 1)
            pos_y = random.randint(0, self.height - 1)
            if self.world_grid[pos_x][pos_y] == EMPTY:
                break

        self.world_grid[pos_x][pos_y] = FOOD

    def spawn_organism(self):
        while True:
            pos_x = random.randint(0, self.width - 1)
            pos_y = random.randint(0, self.height - 1)
            if self.world_grid[pos_x][pos_y] == EMPTY:
                break

        self.world_grid[pos_x][pos_y] = ORGANISM

        # Add new organism to array
        new_dna = DNA(100, 3)
        new_organism = Organism(pos_x, pos_y, new_dna)
        self.organisms.append(new_organism)

    # Here the entire world state will be updated and prepared for redraw in sim window
    def update(self):
        for organism in self.organisms:
            dx, dy = organism.choose_direction()
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
                    # TODO: Add functionality regarding eating food
                    organism.add_energy(20)
            organism.lose_energy(2)
            if not organism.is_alive:
                self.world_grid[organism.x][organism.y] = EMPTY

        self.organisms = [org for org in self.organisms if org.is_alive]