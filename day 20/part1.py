from aocd import get_data
data = get_data(day=20, year=2024)

# data = '''###############
# #...#...#.....#
# #.#.#.#.#.###.#
# #S#...#.#.#...#
# #######.#.#.###
# #######.#.#...#
# #######.#.###.#
# ###..E#...#...#
# ###.#######.###
# #...###...#...#
# #.#####.#.###.#
# #.#...#.#.#...#
# #.#.#.#.#.#.###
# #...#...#...###
# ###############'''

data = data.strip().split('\n')

can_disable = set()

# From 1 to length-1 so I don't need to do range checks
for row in range(1, len(data)-1):
    for col in range(1, len(data[0])-1):
        if data[row][col] != '#':
            continue

        if (data[row+1][col] != '#' and data[row-1][col] != '#') or (data[row][col+1] != '#' and data[row][col-1] != '#'):
            can_disable.add((row, col))

walls = set()
start = None
end = None
for row in range(len(data)):
    for col in range(len(data[0])):
        if data[row][col] == '#':
            walls.add((row, col))
        elif data[row][col] == 'S':
            start = (row, col)
        elif data[row][col] == 'E':
            end = (row, col)

def best_path(start, end, walls, disabled=None):
    queue = [(start, 0)]
    visited = {start}
    for (row, col), dist in queue:
        if (row, col) == end:
            return dist

        for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + dir[0], col + dir[1]

            if (new_row, new_col) == disabled or (new_row, new_col) not in walls and (new_row, new_col) not in visited:
                queue.append(((new_row, new_col), dist+1))
                visited.add((new_row, new_col))

# counts = {}
current = best_path(start, end, walls)
total = 0
for i, disabled in enumerate(can_disable):
    if i % 100 == 0:
        print(i, len(can_disable))
    dist = best_path(start, end, walls, disabled)
    
    # if not (current-dist) in counts:
    #     counts[(current-dist)] = 0
    # counts[(current-dist)] += 1

    if dist <= current - 100:
        total += 1

print(total)
# can be made faster if we stop searching when distance is higher than 100 over current