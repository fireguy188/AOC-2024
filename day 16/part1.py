from aocd import get_data
data = get_data(day=16, year=2024)

# data = '''#################
# #...#...#...#..E#
# #.#.#.#.#.#.#.#.#
# #.#.#.#...#...#.#
# #.#.#.#.###.#.#.#
# #...#.#.#.....#.#
# #.#.#.#.#.#####.#
# #.#...#.#.#.....#
# #.#.#####.#.###.#
# #.#.#.......#...#
# #.#.###.#####.###
# #.#.#...#.....#.#
# #.#.#.#####.###.#
# #.#.#.........#.#
# #.#.#.#########.#
# #S#.............#
# #################'''

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

visited = {(start_row, start_col)}
queue = [(0, start_row, start_col, (0, 1))]
while queue:
    score, row, col, dir = heapq.heappop(queue)

    if (row, col) == (end_row, end_col):
        print(score)
        break

    for new_dir in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        new_row, new_col = row + new_dir[0], col + new_dir[1]
        new_score = score + 1
        if new_dir != dir:
            new_score += 1000
        
        if 0 <= new_row < len(data) and 0 <= new_col < len(data[0]) and data[new_row][new_col] != '#' and (new_row, new_col) not in visited:
            visited.add((new_row, new_col))
            heapq.heappush(queue, (new_score, new_row, new_col, new_dir))
            