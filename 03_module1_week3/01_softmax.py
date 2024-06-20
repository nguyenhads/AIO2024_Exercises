# Softmax Class
import torch
import torch.nn as nn


class Softmax(nn.Module):

    def __init__(self, dim=0):
        super(Softmax, self).__init__()
        self.dim = dim

    def forward(self, x):
        return self.softmax(x)

    def softmax(self, x):
        exp_x = torch.exp(x)
        return exp_x / torch.sum(exp_x, self.dim)

    def softmax_stable(self, x):
        c = torch.max(x)
        exp_x = torch.exp(x - c)
        return exp_x / torch.sum(exp_x, self.dim)


if __name__ == "__main__":
    data = torch.Tensor([1, 2, 3])
    softmax = Softmax()
    output1 = softmax.forward(data)
    output2 = softmax.softmax_stable(data)
    print(output1)
    print(output2)
