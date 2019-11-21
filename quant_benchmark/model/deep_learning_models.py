#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import torch
import torch.nn as nn
import torch.nn.functional as F

# NN1
class NN1(nn.Module):

    def __init__(self, input_size, hidden_size=32, output_size=1):
        super(NN1, self).__init__()

        self.layer1 = nn.Linear(input_size, hidden_size)
        self.layer2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = F.relu(self.layer1(x))
        x = self.layer2(x)
        return x


# NN2
class NN2(nn.Module):

    def __init__(self, input_size, hidden1_size=32, hidden2_size=16, output_size=1):
        super(NN2, self).__init__()

        self.layer1 = nn.Linear(input_size, hidden1_size)
        self.layer2 = nn.Linear(hidden1_size, hidden2_size)
        self.layer3 = nn.Linear(hidden2_size, output_size)

    def forward(self, x):
        x = F.relu(self.layer1(x))
        x = F.relu(self.layer2(x))
        x = self.layer3(x)
        return x


# NN3
class NN3(nn.Module):

    def __init__(self, input_size, hidden1_size=32, hidden2_size=16, hidden3_size=8, output_size=1):
        super(NN3, self).__init__()

        self.layer1 = nn.Linear(input_size, hidden1_size)
        self.layer2 = nn.Linear(hidden1_size, hidden2_size)
        self.layer3 = nn.Linear(hidden2_size, hidden3_size)
        self.layer4 = nn.Linear(hidden3_size, output_size)

    def forward(self, x):
        x = F.relu(self.layer1(x))
        x = F.relu(self.layer2(x))
        x = F.relu(self.layer3(x))
        x = self.layer4(x)
        return x


# NN4
class NN4(nn.Module):

    def __init__(self, input_size, hidden1_size=32, hidden2_size=16, hidden3_size=8, hidden4_size=4, output_size=1):
        super(NN4, self).__init__()

        self.layer1 = nn.Linear(input_size, hidden1_size)
        self.layer2 = nn.Linear(hidden1_size, hidden2_size)
        self.layer3 = nn.Linear(hidden2_size, hidden3_size)
        self.layer4 = nn.Linear(hidden3_size, hidden4_size)
        self.layer5 = nn.Linear(hidden4_size, output_size)

    def forward(self, x):
        x = F.relu(self.layer1(x))
        x = F.relu(self.layer2(x))
        x = F.relu(self.layer3(x))
        x = F.relu(self.layer4(x))
        x = self.layer5(x)
        return x


# NN5
class NN5(nn.Module):

    def __init__(self, input_size, hidden1_size=32, hidden2_size=16, hidden3_size=8, hidden4_size=4, hidden5_size=2, output_size=1):
        super(NN5, self).__init__()

        self.layer1 = nn.Linear(input_size, hidden1_size)
        self.layer2 = nn.Linear(hidden1_size, hidden2_size)
        self.layer3 = nn.Linear(hidden2_size, hidden3_size)
        self.layer4 = nn.Linear(hidden3_size, hidden4_size)
        self.layer5 = nn.Linear(hidden4_size, hidden5_size)
        self.layer6 = nn.Linear(hidden5_size, output_size)

    def forward(self, x):
        x = F.relu(self.layer1(x))
        x = F.relu(self.layer2(x))
        x = F.relu(self.layer3(x))
        x = F.relu(self.layer4(x))
        x = F.relu(self.layer5(x))
        x = self.layer6(x)
        return x


class Paper_nn(nn.Module):
    
    def __init__(self, input_size):
        super(Paper_nn, self).__init__()
        self.layer1 = nn.Linear(input_size, input_size//2)
        self.dp = nn.Dropout(p=0.5)
        self.layer2 = nn.Linear(input_size//2, input_size//4)
        self.bn = nn.BatchNorm1d(input_size//4)
        self.layer3 = nn.Linear(input_size//4, 2)
        
    def forward(self, x):
        x = F.relu(self.layer1(x))
        x = self.dp(x)
        x = F.relu(self.layer2(x))
        x = self.bn(x)
        x = self.layer3(x)
        return x 

if __name__ ==  "__main__":
    batch_size = 5
    input_size = 10
    input_data = torch.randn(batch_size, input_size)
    
    loss_func = nn.MSELoss()
    
    model1 = NN1(input_size=input_size, hidden_size=32, output_size=1)
    output = model1.forward(input_data)
    target = torch.randn_like(output)    
    loss = loss_func(output, target)
    print(loss)
    
    model2 = NN2(input_size=input_size, hidden1_size=32, hidden2_size=16, output_size=1)
    output = model2.forward(input_data)
    target = torch.randn_like(output)    
    loss = loss_func(output, target)
    print(loss)