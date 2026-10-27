import pygame
from core.world import World, EMPTY, FOOD, ORGANISM

class SimWindow:
    def __init__(self, width=120, height=70, cell_size = 10):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        self.screen_width = self.width * self.cell_size
        self.screen_height = self.height * self.cell_size

        self.COLOR_BG = (46, 204, 113)
        self.COLOR_FOOD = (231, 76, 60)
        self.COLOR_ORGANISM = (30, 30, 30)

        self.world = World(width=self.width, height=self.height, num_organisms=10, init_food=100)

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

                screen.fill(self.COLOR_BG)

                # Rysowanie siatki
                for x in range(self.world.width):
                    for y in range(self.world.height):
                        cell_type = self.world.world_grid[x][y]
                        
                        if cell_type == FOOD:
                            pygame.draw.rect(screen, self.COLOR_FOOD, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                        elif cell_type == ORGANISM:
                            pygame.draw.rect(screen, self.COLOR_ORGANISM, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))

                # Odświeżenie ekranu
                pygame.display.flip()
                
                # 10 klatek na sekundę
                clock.tick(10)
                self.world.update()
            pygame.quit()