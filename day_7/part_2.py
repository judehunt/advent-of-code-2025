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
    beam_value = max(row_input)
    beam_index = row_input.index(beam_value)

    if beam_index not in split_indices or len(split_indices) == 0:
        return [row_input]
    else:
        # Return 1 version where it splits left, and 1 where it splits right
        left_split_row = [
            beam_value
            if (i == beam_index - 1)
            or (row_input[i] == beam_value and i not in split_indices)
            else 0
            for i in range(len(row_input))
        ]
        right_split_row = [
            beam_value
            if (i == beam_index + 1)
            or (row_input[i] == beam_value and i not in split_indices)
            else 0
            for i in range(len(row_input))
        ]
        return [left_split_row, right_split_row]


inputs = read_input("day_7/input.txt")

input_row = get_input_row(inputs)

for i, line in enumerate(inputs[1:]):
    print(f"{i + 1}/{len(inputs) - 1}: {line}")
    output_rows = []

    # Construct input rows - one for each possibility
    input_rows = [
        [x if idx_j == idx else 0 for idx_j, x_j in enumerate(input_row)]
        for idx, x in enumerate(input_row)
        if x > 0
    ]

    for input_row in input_rows:
        possible_output_rows = row_split(input_row, line)
        output_rows.extend(possible_output_rows)

    # Sum up the output rows to get total possibilities at each position
    summed_output_row = [0] * len(output_rows[0])
    for output_row in output_rows:
        for i, val in enumerate(output_row):
            summed_output_row[i] += val

    input_row = summed_output_row
    print("=" * 30)

print(f"Final possibilities: {sum(input_row)}")
