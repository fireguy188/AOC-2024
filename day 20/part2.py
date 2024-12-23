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

current_dist = dist

import heapq

total = 0
cheat_size = 20
queue = [(0, start, ((-1, -1), (-1, -1)))]
visited = {(start, ((-1, -1), (-1, -1)))}
best = 0
while queue:
    dist, (row, col), cheat = heapq.heappop(queue)

    if dist > best:
        best = dist
        print(dist, current_dist)

    saved = current_dist - dist

    if saved < 100:
        break

    if (row, col) == end:
        total += 1
        continue

    # Either do a normal movement
    for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_row, new_col = row + dir[0], col + dir[1]

        if data[new_row][new_col] != '#' and ((new_row, new_col), cheat) not in visited:
            heapq.heappush(queue, (dist+1, (new_row, new_col), cheat))
            visited.add(((new_row, new_col), cheat))
    
    # Or do a cheat move
    if cheat == ((-1, -1), (-1, -1)):
        for row_offset in range(-cheat_size, cheat_size+1):
            for col_offset in range(-cheat_size, cheat_size+1):
                if abs(row_offset) + abs(col_offset) > cheat_size:
                    continue

                if row_offset == col_offset == 0:
                    continue

                new_row, new_col = row + row_offset, col + col_offset

                if not(0 <= new_row < len(data) and 0 <= new_col < len(data[0])):
                    continue

                if data[new_row][new_col] == '#':
                    continue

                cheat = ((row, col), (new_row, new_col))

                if ((new_row, new_col), cheat) in visited:
                    continue
                
                heapq.heappush(queue, (dist+abs(row_offset)+abs(col_offset), (new_row, new_col), cheat))
                visited.add(((new_row, new_col), cheat))

print(total)