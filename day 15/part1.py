from aocd import get_data
data = get_data(day=15, year=2024)

# data = '''##########
# #..O..O.O#
# #......O.#
# #.OO..O.O#
# #..O@..O.#
# #O#..O...#
# #O..O..O.#
# #.OO.O.OO#
# #....O...#
# ##########

# <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
# vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
# ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
# <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
# ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
# ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
# >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
# <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
# ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
# v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^'''

maze, moves = data.strip().split('\n\n')
maze = maze.split('\n')
width, height = len(maze[0]), len(maze)
map = {}

for row in range(height):
    for col in range(width):
        map[(row, col)] = maze[row][col]

def get_start():
    for row in range(height):
        for col in range(width):
            if map[(row, col)] == '@':
                return row, col

def print_maze():
    for row in range(height):
        print_row = ''
        for col in range(width):
            print_row += map[(row, col)]
        print(print_row)

row, col = get_start()
for move in moves:
    if move == '<':
        for c in range(col-1, -1, -1):
            if map[(row, c)] == '.':
                # Move everything left
                map[(row, col)] = '.'

                if map[(row, col-1)] == 'O':
                    map[(row, c)] = 'O'

                map[(row, col-1)] = '@'

                col -= 1

                break
            elif map[(row, c)] == '#':
                # Move nothing
                break
    elif move == '>':
        for c in range(col+1, width):
            if map[(row, c)] == '.':
                # Move everything right
                map[(row, col)] = '.'

                if map[(row, col+1)] == 'O':
                    map[(row, c)] = 'O'

                map[(row, col+1)] = '@'

                col += 1

                break
            elif map[(row, c)] == '#':
                # Move nothing
                break
    elif move == 'v':
        for r in range(row+1, height):
            if map[(r, col)] == '.':
                # Move everything down
                map[(row, col)] = '.'

                if map[(row+1, col)] == 'O':
                    map[(r, col)] = 'O'

                map[(row+1, col)] = '@'

                row += 1

                break
            elif map[(r, col)] == '#':
                # Move nothing
                break
    elif move == '^':
        for r in range(row-1, -1, -1):
            if map[(r, col)] == '.':
                # Move everything down
                map[(row, col)] = '.'

                if map[(row-1, col)] == 'O':
                    map[(r, col)] = 'O'

                map[(row-1, col)] = '@'

                row -= 1

                break
            elif map[(r, col)] == '#':
                # Move nothing
                break

total = 0
for row in range(height):
    for col in range(width):
        if map[(row, col)] == 'O':
            total += row * 100 + col
print(total)