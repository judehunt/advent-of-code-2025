def read_ids(file_path):
    with open(file_path, 'r') as file:
        # Read the single line and split by commas
        line = file.readline().strip()
        ids = line.split(',')
    return ids

def get_id_ranges(id_range):
    start, end = id_range.split('-')
    ids = range(int(start), int(end) + 1)
    return ids
    
def validate_id(id):
    id_str = str(id)

    # Get factors of the length of the ID (not including the full length)
    len_id = len(id_str)
    factors = []
    for i in range(1, len_id):
        if len_id % i == 0:
            factors.append(i)

    for segment_length in factors:
        # Get the segments based on the current factor
        segments = [id_str[i:i + segment_length] for i in range(0, len_id, segment_length)]
        segments = set(segments)
        if len(segments) == 1:
            return False

    return True    

ids = read_ids("day_2/input.txt")

invalid_ids = []
for id_range in ids:
    ids = get_id_ranges(id_range)
    for current_id in ids:
        if not validate_id(current_id):
            invalid_ids.append(current_id)
            
print(invalid_ids)
print(sum(invalid_ids)) # 48631958998