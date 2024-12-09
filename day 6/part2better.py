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


def try_turn_right(row, col, direction, visited):
    direction = right[direction]

    while True:
        if direction == 'u':
            if row - 1 < 0 or data[row-1][col] == '#':
                return False

            row, col = row-1, col
        elif direction == 'd':
            if row + 1 >= len(data) or data[row+1][col] == '#':
                return False
            
            row, col = row+1, col
        elif direction == 'l':
            if col - 1 < 0 or data[row][col-1] == '#':
                return False

            row, col = row, col-1
        elif direction == 'r':
            if col + 1 >= len(data[0]) or data[row][col+1] == '#':
                return False

            row, col = row, col+1
        
        if (row, col) in visited and visited[(row, col)] == direction:
            return True

row, col = s_row, s_col
visited = {}
intersections = 0
direction = 'u'
right = {'u':'r', 'r':'d', 'd':'l', 'l':'u'}
while True:
    if direction == 'u':
        if row - 1 < 0:
            break

        if data[row-1][col] == '#':
            direction = right[direction]
        else:
            row, col = row-1, col
    elif direction == 'd':
        if row + 1 >= len(data):
            break

        if data[row+1][col] == '#':
            direction = right[direction]
        else:
            row, col = row+1, col
    elif direction == 'l':
        if col - 1 < 0:
            break

        if data[row][col-1] == '#':
            direction = right[direction]
        else:
            row, col = row, col-1
    elif direction == 'r':
        if col + 1 >= len(data[0]):
            break

        if data[row][col+1] == '#':
            direction = right[direction]
        else:
            row, col = row, col+1
    
    # See if turning right would put us in a pickle
    if try_turn_right(row, col, direction, visited):
        #print(row, col)
        intersections += 1
    visited[(row, col)] = direction
    

print(intersections)