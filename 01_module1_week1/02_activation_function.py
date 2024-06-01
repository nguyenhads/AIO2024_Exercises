# Viết function mô phỏng theo 3 activation function.
import math


# Given funtion
def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


# Activation functions
def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def relu(x):
    return max(0, x)


def elu(x, alpha=0.01):
    if x > 0:
        return x
    else:
        return alpha * (math.exp(x) - 1)


def calculate_activation_function(x, activation_function, alpha=0.01):
    x = float(x)
    if activation_function == "sigmoid":
        result = sigmoid(x)
    elif activation_function == "relu":
        result = relu(x)
    elif activation_function == "elu":
        result = elu(x, alpha)
    else:
        raise ValueError(f"{activation_function} is not supported")

    return result


if __name__ == "__main__":
    x = input("Input x: ")

    if not is_number(x):
        raise ValueError("x must be a number")

    activation_function = input("Input activation function (sigmoid|relu|elu): ")
    result = calculate_activation_function(x=x, activation_function=activation_function)
    print(f"{activation_function}: f({x}) = {result}")
