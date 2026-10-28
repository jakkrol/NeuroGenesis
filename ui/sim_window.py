import pygame
from core.world import World
from core.config import EMPTY, FOOD, ORGANISM, MOVE_COST, MAX_ENERGY, WIDTH, HEIGHT

class SimWindow:
    def __init__(self, cell_size = 10):
        self.width = WIDTH
        self.height = HEIGHT
        self.cell_size = cell_size

        self.screen_width = self.width * self.cell_size
        self.screen_height = self.height * self.cell_size

        self.color_bg = (46, 204, 113)
        self.color_food = (231, 76, 60)
        self.color_organism = (30, 30, 30)

        self.world = World(self.width, self.height, num_organisms=10, init_food=100)

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("NeuroGenesis - Symulacja Życia")
        clock = pygame.time.Clock()

        running = True
        while running:
            # Obsługa zdarzeń
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill(self.color_bg)

            # Rysowanie siatki
            for x in range(self.world.width):
                for y in range(self.world.height):
                    cell_type = self.world.world_grid[x][y]
                    
                    if cell_type == FOOD:
                        pygame.draw.rect(screen, self.color_food, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                    elif cell_type == ORGANISM:
                        pygame.draw.rect(screen, self.color_organism, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))

            # Odświeżenie ekranu
            pygame.display.flip()
            
            clock.tick(10)
            self.world.update()
            
        pygame.quit()