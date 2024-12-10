from aocd import get_data
data = get_data(day=10, year=2024)

# data = '''89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732'''

data = data.strip().split('\n')

def explore(row, col):
    queue = [(row, col)]
    visited = {(row, col)}

    score = 0
    for (row, col) in queue:
        if data[row][col] == '9':
            score += 1
            continue

        adjacent = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        for (new_row, new_col) in adjacent:
            # Range check
            if not(0 <= new_row < len(data) and 0 <= new_col < len(data[0])):
                continue

            # Seen before check
            if (new_row, new_col) in visited:
                continue
            
            # Gradual slope check
            if int(data[new_row][new_col]) != int(data[row][col]) + 1:
                continue

            queue.append((new_row, new_col))
            visited.add((new_row, new_col))
    
    return score
                
total = 0
for row in range(len(data)):
    for col in range(len(data[row])):
        if data[row][col] == '0':
            total += explore(row, col)

print(total)