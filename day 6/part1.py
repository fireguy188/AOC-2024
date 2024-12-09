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

row, col = None, None
direction = 'u'
for r in range(len(data)):
    for c in range(len(data[0])):
        if data[r][c] == '^':
           row, col = r, c

visited = {(row, col)}
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

    visited.add((row, col))

print(len(visited))