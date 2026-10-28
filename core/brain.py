import random
import torch
import torch.nn as nn

DIRECTIONS = [
    (0, -1),
    (1, -1),
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1)
]

class Brain:
    def __init__(self, input_size=25, output_size=8, hidden_size=16):
        super(Brain, self).__init__()

        self.l1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.l2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.l1(x)
        x = self.relu(x)
        x = self.l2(x)
        return x

    def decide(self, inputs):
        # dx = random.choice([1, -1, 0])
        # dy = random.choice([1, -1, 0])
        # return dx, dy
        x = torch.tensor(inputs, dtype=torch.float32)

        with torch.no_grad():
            outputs = self.forward(x)
            action = torch.argmax(outputs).item()

        return DIRECTIONS[action]