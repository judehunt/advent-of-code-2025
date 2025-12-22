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


def find_fresh_ingredients_from_range(fresh_ingredient_ranges):
    num_fresh_ingredients = 0
    for range_idx, fresh_range in enumerate(fresh_ingredient_ranges):
        print(range_idx)
        # Some of the ranges here are massive... Might be more efficient to compare the other way round
        start, end = map(int, fresh_range.split("-"))
        for i in range(start, end + 1):
            # Check if this ingredient was already counted
            # We don't want to keep a list of all found ingredients, so we can do this by checking previous ranges
            print(len(fresh_ingredient_ranges[:range_idx]))
            already_counted = any(
                int(prev_start) <= i <= int(prev_end)
                for prev_range in fresh_ingredient_ranges[:range_idx]
                for prev_start, prev_end in [prev_range.split("-")]
                if prev_range != fresh_range  # Don't compare with the same range
            )
            print(already_counted)
            if not already_counted:
                num_fresh_ingredients += 1

    return num_fresh_ingredients


# inputs = read_input("day_5/test.txt")
inputs = read_input("day_5/input.txt")
fresh_ingredient_ranges, ingredient_list = split_input(inputs)

num_fresh_ingredients = find_fresh_ingredients_from_range(fresh_ingredient_ranges)
print(f"Total fresh ingredients from ranges: {num_fresh_ingredients}")
