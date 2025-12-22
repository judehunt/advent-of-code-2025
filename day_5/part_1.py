def read_input(file_path):
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


def split_input(lines):
    # Split on the blank line
    split_index = lines.index("")
    part1 = lines[:split_index]
    part2 = lines[split_index + 1 :]
    return part1, part2


inputs = read_input("day_5/input.txt")
fresh_ingredient_ranges, ingredient_list = split_input(inputs)

num_fresh_ingredients = 0
for ingredient in ingredient_list:
    ingredient_id = int(ingredient)
    is_fresh = any(
        int(range_start) <= ingredient_id <= int(range_end)
        for fresh_range in fresh_ingredient_ranges
        for range_start, range_end in [fresh_range.split("-")]
    )
    if is_fresh:
        print(f"Fresh ingredient found: {ingredient_id}")
        num_fresh_ingredients += 1

print(f"Total fresh ingredients: {num_fresh_ingredients}")