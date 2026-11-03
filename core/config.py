WIDTH = 140
HEIGHT = 70

EMPTY = 0
FOOD = 1
POISON = 2
ORGANISM = 9
WALL = -1 

MOVE_COST = 5
MAX_ENERGY = 100
FOOD_ENERGY_GAIN = 30
FOOD_ON_MAP = 600
ENERGY_LOSS_ON_TICK = 2
MAX_AGE = 100

DIRECTIONS = [
    (0, -1),  # Góra
    (1, 0),   # Prawo
    (0, 1),   # Dół
    (-1, 0),  # Lewo
    (-1, -1),  # Lewo-góra
    (1, 1),   # Prawo-dół
    (1, -1),  # Prawo-góra
    (-1, 1)   # Lewo-dół
]
