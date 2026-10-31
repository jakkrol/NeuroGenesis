import pygame
from core.world import World
from core.config import FOOD, ORGANISM, POISON

class SimWindow:
    def __init__(self, world, cell_size = 10):
        self.cell_size = cell_size
        self.screen_width = world.width * self.cell_size
        self.screen_height = world.height * self.cell_size

        self.color_bg = (46, 204, 113)
        self.color_food = (231, 76, 60)
        self.color_organism = (30, 30, 30)
        self.color_poison = (155, 89, 182)

        self.world = world

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("NeuroGenesis")
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
                    elif cell_type == POISON:
                        pygame.draw.rect(screen, self.color_poison, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))

            # Odświeżenie ekranu
            pygame.display.flip()
            
            clock.tick(10)
            self.world.step()
            
        pygame.quit()