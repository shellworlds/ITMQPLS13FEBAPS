import torch
import torch.nn as nn
class QuantumNN(nn.Module):
    def forward(self, x):
        return x.mean()
