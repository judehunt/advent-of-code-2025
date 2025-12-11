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


def get_num_rolls(grid):
    return sum(sum(row) for row in grid)


def remove_accessible_points(grid, num_free_neighbours: int = 4):
    results = []
    for i in range(len(grid)):
        row_results = []
        for j in range(len(grid[0])):
            num_neighbors = search_neighbours(grid, i, j)
            # A roll can be accessed if it has less than 4 neighboring @ and is itself an @
            # Only keep the inaccessible points
            roll_left = (
                1 if num_neighbors >= num_free_neighbours and grid[i][j] == 1 else 0
            )
            row_results.append(roll_left)
        results.append(row_results)
    return results


inputs = read_input("day_4/input.txt")
inputs = process_data(inputs)
results = inputs
while True:
    new_results = remove_accessible_points(results, num_free_neighbours=4)
    if new_results == results:
        break
    results = new_results


final_total = get_num_rolls(results)
original_total = get_num_rolls(inputs)
print(
    f"Total accessible locations at the end: {final_total}, originally had: {original_total}"
)
removed = original_total - final_total
print(f"Total removed: {removed}")
