import random
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, Tuple

from .config import EMPTY, ORGANISM, MAX_ENERGY, DIRECTIONS, WALL
from .organism import Organism, DNA
from .rules.base import WorldRule

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.organisms: List[Organism] = []
        self.org_positions: Dict[Tuple[int, int], Organism] = {}
        self.rules: List[WorldRule] = []
        self.passable: Set[int] = {EMPTY}
        self.world_grid = self._empty_grid()




    # -------------- rules ----------------
    def add_rule(self, rule: WorldRule) -> None:
        if self.get_rule(rule.name) is not None:
            return None # Albo error
        self.rules.append(rule)
        rule.on_attach(self)


    def remove_rule(self, rule: WorldRule) -> None:
        if self.get_rule(rule.name) is not None:
            self.rules.remove(rule)
            rule.on_detach(self)
        


    def get_rule(self, name:str) -> Optional[WorldRule]:
        for rule in self.rules:
            if rule.name == name:
                return rule
        return None


    # --------------- grid ------------------
    def _empty_grid(self):
        return [[EMPTY for _ in range(self.height)] for _ in range(self.width)]

    def reset(self) -> None:
        self.world_grid = self._empty_grid()
        self.organisms = []
        self.org_positions = {}

    def scatter(self, cell_code: int, count: int) -> int:
        placed = 0
        for _ in range(count):
            while True:
                pos_x = random.randint(0, self.width - 1)
                pos_y = random.randint(0, self.height - 1)
                if self.world_grid[pos_x][pos_y] == EMPTY:
                    break
            self.world_grid[pos_x][pos_y] = cell_code
            placed += 1
        return placed

    def clear_cells(self, cell_code: int) -> None:
        for x in range(self.width):
            for y in range(self.height):
                if self.world_grid[x][y] == cell_code:
                    self.world_grid[x][y] = EMPTY

    #-------------------- organisms ------------------------
    def kill(self, organism: Organism) -> None:
        organism.is_alive = False
        if self.org_positions.get((organism.x, organism.y)) is organism:
            del self.org_positions[(organism.x, organism.y)]
            self.world_grid[organism.x][organism.y] = EMPTY

    def spawn_organism(self, brain, dna: Optional[DNA] = None, pos: Optional[Tuple[int, int]] = None) -> Optional[Organism]:
        # Dodać obsługę gdy pos istnieje
        while True:
            pos_x = random.randint(0, self.width - 1)
            pos_y = random.randint(0, self.height - 1)
            if self.world_grid[pos_x][pos_y] == EMPTY:
                break
        if dna is None:
            dna = DNA(MAX_ENERGY)
        o = Organism(pos_x, pos_y, dna, brain)
        self.organisms.append(o)
        self.org_positions[(pos_x, pos_y)] = o
        self.world_grid[pos_x][pos_y] = ORGANISM
        return o
    #------------------- step ------------------------------
    def step(self):
        for org in list(self.organisms):
            if org.is_alive == False:
                continue
            org.age += 1
            #org.decide(self.get_orientation(org))
            dx, dy = DIRECTIONS[org.decide(self.get_orientation(org))]
            tx = org.x + dx
            ty = org.y + dy
            self.act(org, tx, ty)
            for rule in self.rules:
                if org.is_alive == False:
                    break
                rule.on_organism_tick(self, org)
            if org.is_alive == False:
                self.kill(org)
        self.organisms = [o for o in self.organisms if o.is_alive]


    def get_orientation(self, organism: Organism):
        vision = []
        for dx, dy in DIRECTIONS:
            tx = organism.x + dx
            ty = organism.y + dy
            if not (0 <= tx < self.width and 0 <= ty < self.height):
                vision.append(WALL)
            else:
                vision.append(self.world_grid[tx][ty])
        return vision
        

    def act(self, organism: Organism, x: int, y: int):
        if not (0 <= x < self.width and 0 <= y < self.height):
            return                     

        content = self.world_grid[x][y]

        if content in self.passable:
            self.world_grid[organism.x][organism.y] = EMPTY
            del self.org_positions[(organism.x, organism.y)]
            organism.x, organism.y = x, y
            self.world_grid[organism.x][organism.y] = ORGANISM
            self.org_positions[(x, y)] = organism  
            for rule in self.rules:
                rule.on_enter(self, organism, x, y, content)                
        else:
            for rule in self.rules:
                rule.on_blocked(self, organism, x, y, content)







    # def spawn_organism(self, brain=None):
    #     while True:
    #         pos_x = random.randint(0, self.width - 1)
    #         pos_y = random.randint(0, self.height - 1)
    #         if self.world_grid[pos_x][pos_y] == EMPTY:
    #             break

    #     self.world_grid[pos_x][pos_y] = ORGANISM

    #     # Add new organism to array
    #     new_dna = DNA(100, 3)
    #     new_organism = Organism(pos_x, pos_y, new_dna, brain)
    #     self.organisms.append(new_organism)



    # # Here the entire world state will be updated and prepared for redraw in sim window
    # def update(self):
    #     for organism in self.organisms:
    #         if not organism.is_alive:
    #             continue

    #         organism.age += 1
    #         dx, dy = organism.choose_direction(self.world_grid)
    #         new_x = organism.x + dx
    #         new_y = organism.y + dy

    #         if 0 <= new_x < self.width and 0 <= new_y < self.height:
    #             target = self.world_grid[new_x][new_y]
    #             if target == EMPTY:
    #                 self.world_grid[organism.x][organism.y] = EMPTY
    #                 organism.x = new_x
    #                 organism.y = new_y
    #                 self.world_grid[organism.x][organism.y] = ORGANISM
    #             elif target == FOOD:
    #                 self.world_grid[organism.x][organism.y] = EMPTY
    #                 organism.x = new_x
    #                 organism.y = new_y
    #                 self.world_grid[organism.x][organism.y] = ORGANISM
    #                 organism.add_energy(20)
                    
    #         organism.lose_energy(2)
    #         if not organism.is_alive:
    #             self.world_grid[organism.x][organism.y] = EMPTY

    #     # Sprawdzamy, czy KTÓRYKOLWIEK organizm jeszcze żyje.
    #     any_alive = any(org.is_alive for org in self.organisms)
    #     if not any_alive:
    #         self.check_generation_end()


