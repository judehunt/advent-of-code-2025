def load_data(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

def find_largest_joltage(bank):
    # Get the maximum joltage from the bank (exluding the last element)
    max_joltage = max(bank[:-1])
    # Find the index of the maximum joltage
    max_index = bank.index(max_joltage)

    # And then the maximum that occurs after that value in the sequence
    subsequence = bank[max_index + 1:]
    # Find the maximum in the subsequence
    max_sub_joltage = max(subsequence)
    total_max_joltage = int(str(max_joltage) + str(max_sub_joltage))
    print(f"Max joltage: {max_joltage}, Max subsequence joltage: {max_sub_joltage}, Combined: {total_max_joltage}")
    return total_max_joltage

if __name__ == "__main__":
    data = load_data('day_3/input.txt')
    joltages = [find_largest_joltage(d) for d in data]
    result = sum(joltages)
    print(f"Largest joltage combination: {result}")
