import numpy as np


def read_array(file_path):
    # txt file is a grid of numbers with multiple spaces between each number
    with open(file_path, "r") as f:
        array = [[x for x in line.strip().split() if x] for line in f.readlines()]
    return array


def prepare_data(inputs):
    # Operations for each equation is the last row
    operations = inputs[-1]
    inputs = np.array(inputs[:-1]).astype(int)
    return inputs, operations


def perform_calculations(inputs, operations):
    total = 0
    for i in range(inputs.shape[1]):
        col = inputs[:, i]
        op = operations[i]
        if op == "+":
            col_result = np.sum(col)
        elif op == "*":
            col_result = np.prod(col)
        total += col_result
    return total


inputs = read_array("day_6/input.txt")
inputs, operations = prepare_data(inputs)
total = perform_calculations(inputs, operations)
print(f"Total of all column results: {total}")
