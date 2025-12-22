from tqdm import tqdm


def read_input(file_path):
    with open(file_path, "r") as f:
        input = [line.strip() for line in f.readlines()]
    return input


def split_input(input):
    # Split on the blank line
    split_index = input.index("")
    part1 = input[:split_index]
    part2 = input[split_index + 1 :]
    return part1, part2


def merge_ranges(ranges):
    merged = []
    for current in sorted(ranges, key=lambda x: int(x.split("-")[0])):
        if not merged:
            merged.append(current)
        else:
            last = merged[-1]
            last_start, last_end = map(int, last.split("-"))
            current_start, current_end = map(int, current.split("-"))
            if current_start <= last_end + 1:  # Overlap or contiguous
                merged[-1] = f"{last_start}-{max(last_end, current_end)}"
            else:
                merged.append(current)
    return merged


def find_fresh_ingredients_from_merged_ranges(fresh_ingredient_ranges):
    # Merge overlapping ranges first to avoid double counting
    merged_ranges = merge_ranges(fresh_ingredient_ranges)
    num_fresh_ingredients = 0
    for fresh_range in merged_ranges:
        start, end = map(int, fresh_range.split("-"))
        num_fresh_ingredients += end - start + 1
    return num_fresh_ingredients

inputs = read_input("day_5/input.txt")
fresh_ingredient_ranges, ingredient_list = split_input(inputs)

num_fresh_ingredients = find_fresh_ingredients_from_merged_ranges(
    fresh_ingredient_ranges
)
print(f"Total fresh ingredients from ranges: {num_fresh_ingredients}")
