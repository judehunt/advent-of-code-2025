def load_data(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

def find_largest_joltage(bank, num_switches=2):

    max_joltages = []
    start_index = 0
    for i in range(num_switches):
        subsequence = bank[start_index:-(num_switches - i - 1 )] if (num_switches - i - 1) != 0 else bank[start_index:]
        max_joltage = max(subsequence)
        start_index = subsequence.index(max_joltage) + start_index + 1
        max_joltages.append(max_joltage)
    total_max_joltage = int(''.join(str(j) for j in max_joltages))
    print("="*30)

    return total_max_joltage

if __name__ == "__main__":
    data = load_data('day_3/input.txt')
    joltages = [find_largest_joltage(d, 12) for d in data]

    result = sum(joltages)
    print(f"Largest joltage combination: {result}")