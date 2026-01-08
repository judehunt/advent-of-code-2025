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
    split_indices = [i for i, char in enumerate(row_splitter) if char == "^"]
    assert 1 in row_input, "No beam in input row to split"
    beam_index = row_input.index(1)

    if beam_index not in split_indices or len(split_indices) == 0:
        return [row_input]
    else:
        # Return 1 version where it splits left, and 1 where it splits right
        left_split_row = [
            1
            if (i == beam_index - 1) or (row_input[i] == 1 and i not in split_indices)
            else 0
            for i in range(len(row_input))
        ]
        right_split_row = [
            1
            if (i == beam_index + 1) or (row_input[i] == 1 and i not in split_indices)
            else 0
            for i in range(len(row_input))
        ]
        return [left_split_row, right_split_row]


inputs = read_input("day_7/input.txt")
# inputs = read_input("day_7/test.txt")

input_row = get_input_row(inputs)
input_rows = [input_row]

for i, line in enumerate(inputs[1:]):
    print(f"{i + 1}/{len(inputs) - 1}: {line}")
    output_rows = []
    for input_row in input_rows:
        possible_output_rows = row_split(input_row, line)
        output_rows.extend(possible_output_rows)
    print(f"Number of output rows: {len(output_rows)}")

    input_rows = output_rows
    print("=" * 30)

print(f"Final possibilities: {len(output_rows)}")
