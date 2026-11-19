import torch
import copy
import torch.nn as nn
from ..config import DIRECTIONS
from .base import BaseBrain

class GA(nn.Module, BaseBrain):
    def __init__(self, input_size = len(DIRECTIONS) + 1, output_size = len(DIRECTIONS), hidden = 64, add_dims = 0):
        nn.Module.__init__(self)
        BaseBrain.__init__(self, add_dims=add_dims)
        pass