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

start = None
end = None
for row in range(len(data)):
    for col in range(len(data[0])):
        if data[row][col] == 'S':
            start = (row, col)
        elif data[row][col] == 'E':
            end = (row, col)

# Take some inspiration from Dijkstra day

queue = [(start, 0)]
visited = {start}
for (row, col), dist in queue:
    if (row, col) == end:
        break

    for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_row, new_col = row + dir[0], col + dir[1]

        if data[new_row][new_col] != '#' and (new_row, new_col) not in visited:
            queue.append(((new_row, new_col), dist+1))
            visited.add((new_row, new_col))

path_length = dist

start_to_pos = {}
pos_to_end = {}
for pos, dist in queue:
    start_to_pos[pos] = dist
    pos_to_end[pos] = path_length - dist

def get_dist(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

# total = 0
# for pos1 in start_to_pos:
#     for pos2 in pos_to_end:
#         dist = get_dist(pos1, pos2)
#         if 0 < dist <= 20:
#             # We can cheat between these 2 positions
#             new_path_length = start_to_pos[pos1] + dist + pos_to_end[pos2]

#             if path_length - new_path_length >= 100:
#                 total += 1

total = 0
for pos1 in start_to_pos:
    for row_off in range(-20, 20+1):
        for col_off in range(abs(row_off)-20, -abs(row_off)+20+1):
            # We can cheat between these 2 positions
            pos2 = (pos1[0] + row_off, pos1[1] + col_off)

            if not pos2 in pos_to_end:
                continue

            new_path_length = start_to_pos[pos1] + abs(row_off) + abs(col_off) + pos_to_end[pos2]

            if path_length - new_path_length >= 100:
                total += 1

print(total)