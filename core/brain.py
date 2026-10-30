import random
import torch
import copy
import torch.nn as nn

# DIRECTIONS = [
#     (0, -1),
#     (1, -1),
#     (1, 0),
#     (1, 1),
#     (0, 1),
#     (-1, 1),
#     (-1, 0),
#     (-1, -1)
# ]

DIRECTIONS = [
    (0, -1),   # 0: Góra
    (1, 0),    # 1: Prawo
    (0, 1),    # 2: Dół
    (-1, 0)    # 3: Lewo
]

class Brain(nn.Module):
    def __init__(self, input_size=5, output_size=4, hidden_size=16):
        super(Brain, self).__init__()

        # self.input = nn.Linear(input_size, hidden_size)
        # self.gelu = nn.GELU()
        # self.hidden2 = nn.Linear(hidden_size, hidden_size)
        # self.gelu2 = nn.GELU()
        # self.output = nn.Linear(hidden_size, output_size)

        self.fc = nn.Linear(input_size, output_size)
    def forward(self, x):
        # x = self.input(x)
        # x = self.gelu(x)
        # x = self.hidden2(x)
        # x = self.gelu2(x)
        # x = self.output(x)
        x = self.fc(x)
        return x

    def decide(self, inputs):
        # dx = random.choice([1, -1, 0])
        # dy = random.choice([1, -1, 0])
        # return dx, dy
        x = torch.tensor(inputs, dtype=torch.float32)
        # print(x)
        with torch.no_grad():
            outputs = self.forward(x)
            action = torch.argmax(outputs).item()

        return DIRECTIONS[action]


def mutate(brain):
    child_b = copy.deepcopy(brain)

    with torch.no_grad():
        for param in child_b.parameters():
            mask = torch.randn_like(param) < 0.2
            noise = torch.randn_like(param) * 0.1
            param.add_(noise*mask.float())
    return child_b
    pass
