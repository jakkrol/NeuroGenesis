import torch
import copy
import torch.nn as nn
from ..config import DIRECTIONS

class MLP(nn.Module):
    def __init__(self, input_size = len(DIRECTIONS) + 1, output_size = len(DIRECTIONS), hidden = 16, add_dims = 0):
        super(MLP, self).__init__()
        self.input_size = input_size + add_dims
        self.output_size = output_size

        self.input = nn.Linear(input_size, hidden)
        self.relu = nn.ReLU()
        self.hidden = nn.Linear(hidden, hidden)
        self.relu2 = nn.ReLU()
        self.output  = nn.Linear(hidden, output_size)

        #self.fc = nn.Linear(self.input_size, self.output_size)

    def decide(self, input):
        #print(input)
        x = torch.tensor(input, dtype=torch.float32)
        with torch.no_grad():
            out = self.forward(x)
            action = torch.argmax(out).item()
        return action

    def forward(self, x):
        x = self.input(x)
        x = self.relu(x)
        x = self.hidden(x)
        x = self.relu2(x)
        x = self.output(x)
        #x = self.fc(x)
        return(x)


    def clone(self):
        return copy.deepcopy(self)

    def mutate(self):
        mutated = self.clone()
        with torch.no_grad():
            for param in mutated.parameters():
                mask = torch.randn_like(param) < 0.4
                noise = torch.randn_like(param) * 0.2
                param.add_(mask * noise)
        return mutated
    