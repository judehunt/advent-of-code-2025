def read_input(file_path):
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


def get_input_row(inputs):
    initial_row = inputs[0]
    return [1 if char == "S" else 0 for char in initial_row]


def get_num_splits_in_row(row_input, row_splitter):
    split_indices = [i for i, char in enumerate(row_splitter) if char == "^"]
    num_splits = len([i for i in split_indices if row_input[i] == 1])
    return num_splits


def row_split(row_input, row_splitter):
    # row_input is a list of where the beams are e.g. [0, 0, 0, 1, 0, 0, 0]
    # row splitter is where the splits are from the input e.g. '...^...'
    # And then the row splits the input to either side of the beam, e.g. [0, 0, 1, 0, 1, 0, 0]
    split_indices = [i for i, char in enumerate(row_splitter) if char == "^"]

    # Calculate split row - only split if there's a beam in the input row
    output_row = [
        1
        if any(
            [
                (abs(i - split_index) == 1) and (row_input[split_index] == 1)
                for split_index in split_indices
            ]
        )
        or (row_input[i] == 1 and i not in split_indices)
        else 0
        for i in range(len(row_input))
    ]

    return output_row


inputs = read_input("day_7/input.txt")

input_row = get_input_row(inputs)

total_splits = 0
for line in inputs[1:]:
    row_splits = get_num_splits_in_row(input_row, line)
    input_row = row_split(input_row, line)

    total_splits += row_splits
print("Total splits:", total_splits)
