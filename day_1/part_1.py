
def read_inputs(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]
    
def process_data(data):
    # Return a tuple of L/R and the int to move
    return [(line[0], int(line[1:])) for line in data]

def move_left(position, value):
    # If we move left, we decrease the position
    # But if we go below 0, we wrap around to 99

    return (position - value) % 100

def move_right(position, value):
    # If we move right, we increase the position
    # But if we go above 99, we wrap around to 0
    return (position + value) % 100
    
INITIAL_POSITION = 50
inputs = read_inputs('day-1/inputs.txt')
inputs = process_data(inputs)

zero_counts = 0
for direction, value in inputs:
    print(f"Current position: {INITIAL_POSITION}, moving {direction}{value}")
    if direction == 'L':
        INITIAL_POSITION = move_left(INITIAL_POSITION, value)
        print(f"Moved left to {INITIAL_POSITION}")
    elif direction == 'R':
        INITIAL_POSITION = move_right(INITIAL_POSITION, value)
        print(f"Moved right to {INITIAL_POSITION}")
    if INITIAL_POSITION == 0:
        zero_counts += 1

# 245 too low
print(f"Number of times position 0 was reached: {zero_counts}")