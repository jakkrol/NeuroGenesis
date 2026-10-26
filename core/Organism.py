class Organism:
    def __init__(self, x, y, dna):
        self.x = x
        self.y = y
        self.dna = dna
        self.energy = self.dna.max_energy
        self.speed = self.dna.speed

class DNA:
    def __init__(self, max_energy, speed):
        self.max_energy = max_energy
        self.speed = speed