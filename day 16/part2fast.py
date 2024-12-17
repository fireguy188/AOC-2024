from aocd import get_data
data = get_data(day=16, year=2024)

# data = '''###############
# #.......#....E#
# #.#.###.#.###.#
# #.....#.#...#.#
# #.###.#####.#.#
# #.#.#.......#.#
# #.#.#####.###.#
# #...........#.#
# ###.#.#####.#.#
# #...#.....#.#.#
# #.#.#.###.#.#.#
# #.....#...#.#.#
# #.###.#.#.#.#.#
# #S..#.....#...#
# ###############'''

data = data.strip().split('\n')

import heapq

start_row, start_col = -1, -1
end_row, end_col = -1, -1
for row in range(len(data)):
    for col in range(len(data[0])):
        if data[row][col] == 'S':
            start_row, start_col = row, col
        elif data[row][col] == 'E':
            end_row, end_col = row, col

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def get_shortest_paths(start_row, start_col, start_dir):
    visited = {(start_row, start_col, start_dir): 0}
    queue = [(0, start_row, start_col, start_dir)]
    while queue:
        score, row, col, dir = heapq.heappop(queue)

        for new_dir in dirs:
            if new_dir == dir:
                new_score = score + 1
                new_row, new_col = row + new_dir[0], col + new_dir[1]
            else:
                new_score = score + 1000
                new_row, new_col = row, col
            
            if data[new_row][new_col] != '#' and (new_row, new_col, new_dir) not in visited:
                visited[(new_row, new_col, new_dir)] = new_score
                heapq.heappush(queue, (new_score, new_row, new_col, new_dir))

    return visited

start_to_pos = get_shortest_paths(start_row, start_col, (0, 1))

best_score = float('inf')
for dir in dirs:
    if (end_row, end_col, dir) in start_to_pos:
        best_score = min(best_score, start_to_pos[(end_row, end_col, dir)])

pos_to_end = {}
for end_dir in dirs:
    new_data = get_shortest_paths(end_row, end_col, end_dir)
    for (row, col, dir) in new_data:
        rev_dir = dirs[(dirs.index(dir) + 2) % 4]
        pos_to_end[(row, col, rev_dir)] = min(new_data[(row, col, dir)], pos_to_end.get((row, col, rev_dir), float('inf')))

tiles = set()
for (row, col, dir) in start_to_pos:
    if start_to_pos[(row, col, dir)] + pos_to_end.get((row, col, dir), float('inf')) == best_score:
        tiles.add((row, col))
print(len(tiles))