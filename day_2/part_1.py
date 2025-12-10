def read_ids(file_path):
    with open(file_path, 'r') as file:
        # Read the single line and split by commas
        line = file.readline().strip()
        ids = line.split(',')
    return ids

def get_id_ranges(id):
    start, end = id.split('-')
    ids = list(range(int(start), int(end) + 1))
    return ids
    
def validate_id(id):

    # ID must be valid if odd number of digits
    if len(str(id)) % 2 != 0:
        return True
    
    # Otherwise split the ID into two halves
    id_str = str(id)
    mid = len(id_str) // 2
    first_half = id_str[:mid]
    second_half = id_str[mid:]
    if first_half == second_half:
        return False
    return True
    

ids = read_ids("day_2/input.txt")

invalid_ids = []
for id_range in ids:
    id_list = get_id_ranges(id_range)
    for id in id_list:
        if not validate_id(id):
            invalid_ids.append(id)
            
print(invalid_ids)
print(sum(invalid_ids))