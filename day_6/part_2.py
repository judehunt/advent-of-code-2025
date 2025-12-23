import numpy as np


def read_array(file_path):
    # txt file is a grid of numbers with multiple spaces between each number
    with open(file_path, "r") as f:
        lines = f.readlines()
        array = []
        # The last row is a bunch of characters and spaces
        # And the character is always the first in that column, but the columns can have different numbers of digits
        # So we need to find where that column starts by where that character is in the line
        # Read the last line to find the positions of the characters
        last_line = lines[-1]
        positions = [
            i for i, char in enumerate(last_line) if char != " " and char != "\n"
        ]
        # Add the end position
        positions.append(len(last_line) + 1)

        for line in lines:
            row = []
            for i in range(len(positions) - 1):
                value = line[positions[i] : positions[i + 1] - 1]
                row.append(value)
            array.append(row)
    return array


def parse_column(col):
    col_numbers = []
    # Split the column into individual characters
    max_len_in_col = max(len(col[row].strip()) for row in range(len(col)))
    for digit in range(max_len_in_col):
        current_col_number = ""
        for row in range(len(col)):
            # First number is the rightmost digit of each row
            # Then move leftwards
            num_str = col[row]
            # Check that the digit exists in the number
            # Get the character at position -1 - digit
            character = num_str[-1 - digit]
            if character != " ":
                current_col_number += character
        if current_col_number != "":
            col_numbers.append(int(current_col_number))
    return col_numbers


def prepare_data(inputs):
    # Operations for each equation is the last row
    operations = inputs[-1]
    operations = [op.strip() for op in operations]
    inputs = np.array(inputs[:-1])
    return inputs, operations


def perform_calculations(inputs, operations):
    total = 0
    for i in range(inputs.shape[1]):
        col = inputs[:, i]
        col = parse_column(col)
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
