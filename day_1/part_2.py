
def read_inputs(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]
    
def process_data(data):
    # Return a tuple of L/R and the int to move
    return [(line[0], int(line[1:])) for line in data]

def move_left(position, value):
    # If we move left, we decrease the position
    # But if we go below 0, we wrap around to 99

    new_position = (position - value) % 100
    # Number of times we wrapped around
    zero_ticks = (value - position - 1) // 100 + 1 if value > position else 0

    # # Number of times we wrapped around
    # Adjust for exact hits on 0
    if new_position == 0:
        zero_ticks += 1
    # Adjust for initial position being 0
    if position == 0:
        zero_ticks -= 1

    return new_position, zero_ticks

def move_right(position, value):
    # If we move right, we increase the position
    # But if we go above 99, we wrap around to 0
    new_position = (position + value) % 100
    
    # Number of times we wrapped around or ended at zero
    zero_ticks = (position + value) // 100

    return new_position, zero_ticks
    
INITIAL_POSITION = 50
print(f"The dial starts by pointing at {INITIAL_POSITION}")

inputs = read_inputs('day_1/inputs.txt')
inputs = process_data(inputs)

zero_counts = 0
for direction, value in inputs:
    if direction == 'L':
        INITIAL_POSITION, zero_ticks = move_left(INITIAL_POSITION, value)
    elif direction == 'R':
        INITIAL_POSITION, zero_ticks = move_right(INITIAL_POSITION, value)
    log_str = f"The dial is rotated {direction}{value} to point at {INITIAL_POSITION}"
    if zero_ticks > 0:
        log_str += f"; during this rotation, it points at zero {zero_ticks} time(s)."
    print(log_str)
    zero_counts += zero_ticks

# 5872
print(f"Number of times position 0 was reached: {zero_counts}")