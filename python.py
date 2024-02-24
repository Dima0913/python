import os
def write_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)
def read_from_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data
def get_best_result(filename):
    if os.path.exists(filename):
        return int(read_from_file(filename))
    else:
        return 0
def update_best_result(filename, new_result):
    current_best = get_best_result(filename)
    if new_result > current_best:
        write_to_file(filename, str(new_result))
filename = 'best_result.txt'

best_result = get_best_result(filename)
print("Best result:", best_result)

new_result = 150  
update_best_result(filename, new_result)

best_result = get_best_result(filename)
print("New best result:", best_result)