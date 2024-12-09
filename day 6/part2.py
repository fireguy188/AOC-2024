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

data = data.split('\n')

s_row, s_col = None, None
for r in range(len(data)):
    for c in range(len(data[0])):
        if data[r][c] == '^':
           s_row, s_col = r, c

def does_loop(data, row, col):
    visited = {(row, col, 'u')}
    direction = 'u'
    while True:
        if direction == 'u':
            if row - 1 < 0:
                break

            if data[row-1][col] == '#':
                direction = 'r'
                continue

            row, col = row-1, col
        elif direction == 'd':
            if row + 1 >= len(data):
                break

            if data[row+1][col] == '#':
                direction = 'l'
                continue

            row, col = row+1, col
        elif direction == 'l':
            if col - 1 < 0:
                break

            if data[row][col-1] == '#':
                direction = 'u'
                continue

            row, col = row, col-1
        elif direction == 'r':
            if col + 1 >= len(data[0]):
                break

            if data[row][col+1] == '#':
                direction = 'd'
                continue

            row, col = row, col+1

        if (row, col, direction) in visited:
            return True
        visited.add((row, col, direction))
    
    return False

total = 0
for row in range(len(data)):
    print(row, len(data))
    for col in range(len(data[0])):
        if row == s_row and col == s_col:
            continue

        new_data = data.copy()
        new_data[row] = new_data[row][:col] + '#' + new_data[row][col+1:]
        
        if does_loop(new_data, s_row, s_col):
            total += 1

print(total)