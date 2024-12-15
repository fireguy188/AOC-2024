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
        if maze[row][col] == 'O':
            map[(row, col*2)] = '['
            map[(row, col*2 + 1)] = ']'
        elif maze[row][col] == '@':
            map[(row, col*2)] = '@'
            map[(row, col*2 + 1)] = '.'
        else:
            map[(row, col*2)] = maze[row][col]
            map[(row, col*2 + 1)] = maze[row][col]

width *= 2

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

# print_maze()
# print()
# Left and right box pushes don't change really
# For up and down, we have to handle pushing of multiple boxes
# Keep track of 

row, col = get_start()
for move in moves:
    if move == '<':
        for c in range(col-1, -1, -1):
            if map[(row, c)] == '.':
                # Move everything left
                map[(row, col)] = '.'

                if map[(row, col-1)] == ']':
                    for box_col in range(c+1, col):
                        map[(row, box_col-1)] = map[(row, box_col)]

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

                if map[(row, col+1)] == '[':
                    for box_col in range(c-1, col, -1):
                        map[(row, box_col+1)] = map[(row, box_col)]

                map[(row, col+1)] = '@'

                col += 1

                break
            elif map[(row, c)] == '#':
                # Move nothing
                break
    elif move == 'v':
        # check_cols will store all columns we are moving up on
        # initially this will just store the column of the @ symbol
        # but as we push more boxes, we will add the columns these boxes are in
        hash_reached = False
        check_cols = {col}
        positions_to_move = {(row, col)}
        for r in range(row+1, height):
            new_check_cols = set()
            dot_reached = True
            for c in check_cols:
                if map[(r, c)] == '#':
                    # No more movement
                    hash_reached = True
                    dot_reached = False
                    break

                if map[(r, c)] == '[':
                    new_check_cols.add(c)
                    positions_to_move.add((r, c))
                    new_check_cols.add(c+1)
                    positions_to_move.add((r, c+1))
                    dot_reached = False
                elif map[(r, c)] == ']':
                    new_check_cols.add(c)
                    positions_to_move.add((r, c))
                    new_check_cols.add(c-1)
                    positions_to_move.add((r, c-1))
                    dot_reached = False

            check_cols = new_check_cols

            if hash_reached or dot_reached:
                # No more checking is needed
                start_row = r
                break
        
        if dot_reached:
            # We can start moving everything down
            #print(positions_to_move)
            for r in range(start_row-1, row-1, -1):
                for c in range(width):
                    if (r, c) in positions_to_move:
                        map[(r+1, c)] = map[(r, c)]
                        map[(r, c)] = '.'
            
            row += 1
    elif move == '^':
        # check_cols will store all columns we are moving up on
        # initially this will just store the column of the @ symbol
        # but as we push more boxes, we will add the columns these boxes are in
        hash_reached = False
        check_cols = {col}
        positions_to_move = {(row, col)}
        for r in range(row-1, -1, -1):
            new_check_cols = set()
            dot_reached = True
            for c in check_cols:
                if map[(r, c)] == '#':
                    # No more movement
                    hash_reached = True
                    dot_reached = False
                    break

                if map[(r, c)] == '[':
                    new_check_cols.add(c)
                    positions_to_move.add((r, c))
                    new_check_cols.add(c+1)
                    positions_to_move.add((r, c+1))
                    dot_reached = False
                elif map[(r, c)] == ']':
                    new_check_cols.add(c)
                    positions_to_move.add((r, c))
                    new_check_cols.add(c-1)
                    positions_to_move.add((r, c-1))
                    dot_reached = False

            check_cols = new_check_cols

            if hash_reached or dot_reached:
                # No more checking is needed
                start_row = r
                break
        
        if dot_reached:
            # We can start moving everything down
            #print(positions_to_move)
            for r in range(start_row+1, row+1):
                for c in range(width):
                    if (r, c) in positions_to_move:
                        map[(r-1, c)] = map[(r, c)]
                        map[(r, c)] = '.'
            
            row -= 1

total = 0
for row in range(height):
    for col in range(width):
        if map[(row, col)] == '[':
            total += row * 100 + col
print(total)