# Essentially a convolutional filter over here to get the sum around (excluding the central cell)
def read_input(file_path):
    with open(file_path, "r") as f:
        grid = [list(line.strip()) for line in f.readlines()]
    return grid


def process_data(grid):
    # Convert grid to integers - 1 if @, 0 if .
    int_grid = [[1 if cell == "@" else 0 for cell in row] for row in grid]
    return int_grid


def search_neighbours(grid, x, y):
    # All 8 possible directions around the point to search
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    total = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        # Exclude out of bounds
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            total += grid[nx][ny]
    return total


inputs = read_input("day_4/input.txt")
inputs = process_data(inputs)
results = []
for i in range(len(inputs)):
    row_results = []
    for j in range(len(inputs[0])):
        num_neighbors = search_neighbours(inputs, i, j)
        # A roll can be accessed if it has less than 4 neighboring @ and is itself an @
        can_access = 1 if num_neighbors < 4 and inputs[i][j] == 1 else 0
        row_results.append(can_access)
    results.append(row_results)

print(results)
total_accessible = sum(sum(row) for row in results)
print(f"Total accessible locations: {total_accessible}")
