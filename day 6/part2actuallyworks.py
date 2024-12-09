from aocd import get_data
data = get_data(day=6, year=2024)

# data = '''....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...'''

# data = '''..........
# ..........
# ..........
# ..........
# ....#.....
# ....##....
# ....^#....
# ...##.....
# ..........
# ..........'''

data = data.split('\n')
right = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}

s_row, s_col = None, None
for r in range(len(data)):
    for c in range(len(data[0])):
        if data[r][c] == '^':
           s_row, s_col = r, c

def does_loop(s_row, s_col, direction, data):
    row, col = s_row, s_col
    visited_directions = set()

    # Calculate initial path
    while 0 <= row < len(data) and 0 <= col < len(data[0]):
        if (row, col, direction) in visited_directions:
            return True
        visited_directions.add((row, col, direction))

        new_row, new_col = row + direction[0], col + direction[1]

        if 0 <= new_row < len(data) and 0 <= new_col < len(data[0]) and data[new_row][new_col] == '#':
            direction = right[direction]
        else:
            row, col = new_row, new_col
    
    return False

row, col = s_row, s_col
direction = (-1, 0)
visited = set()
total = 0
while 0 <= row < len(data) and 0 <= col < len(data[0]):
    visited.add((row, col))
    new_row, new_col = row + direction[0], col + direction[1]

    if 0 <= new_row < len(data) and 0 <= new_col < len(data[0]) and data[new_row][new_col] == '#':
        direction = right[direction]
    else:
        if 0 <= new_row < len(data) and 0 <= new_col < len(data[0]) and not (new_row, new_col) in visited:
            new_data = data.copy()
            new_data[new_row] = new_data[new_row][:new_col] + '#' + new_data[new_row][new_col+1:]
            if does_loop(row, col, direction, new_data):
                total += 1
        row, col = new_row, new_col

print(total)