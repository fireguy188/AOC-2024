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

# Find score of best path
def shortest(start_row, start_col, end_row, end_col, start_dir, end_dir=None):
    visited = {(start_row, start_col, start_dir)}
    queue = [(0, start_row, start_col, start_dir)]
    while queue:
        score, row, col, dir = heapq.heappop(queue)

        if (row, col) == (end_row, end_col) and (end_dir == None or dir == end_dir):
            return score

        for new_dir in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            new_row, new_col = row + new_dir[0], col + new_dir[1]
            new_score = score + 1
            if new_dir != dir:
                new_score += 1000
            
            if data[new_row][new_col] != '#' and (new_row, new_col, new_dir) not in visited:
                visited.add((new_row, new_col, new_dir))
                heapq.heappush(queue, (new_score, new_row, new_col, new_dir))
    
    return float('inf')

best_score = shortest(start_row, start_col, end_row, end_col, (0, 1))

# Go through every empty position
# if best score from start to pos + best score from pos to end = best path score
# the position is part of a best path
def is_best_path(row, col):
    best = float('inf')
    for dir1 in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        best = min(best, 
                shortest(start_row, start_col, row, col, (0, 1), dir1) + 
                shortest(row, col, end_row, end_col, dir1))
        if best == best_score:
            return True
    return False

total = 0
for row in range(len(data)):
    print(row, len(data))
    for col in range(len(data[0])):
        if data[row][col] != '#' and is_best_path(row, col):
            total += 1
print(total)
# 519 too low, 550 too high


# Find all best paths
# now we will store connections in visited rather than individual positions
# visited = set()
# queue = [(0, start_row, start_col, (0, 1), ((start_row, start_col),))]
# tiles = set()
# while queue:
#     score, row, col, dir, path = heapq.heappop(queue)

#     if (10, 1) in path:
#         print(path)

#     if (row, col) == (end_row, end_col):
#         #print(path, score)
#         for tile in path:
#             tiles.add(tile)
#         continue

#     for new_dir in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
#         new_row, new_col = row + new_dir[0], col + new_dir[1]
#         new_score = score + 1
#         if new_dir != dir:
#             new_score += 1000
#         new_path = path + ((new_row, new_col),)
        
#         if data[new_row][new_col] != '#' and ((row, col), (new_row, new_col)) not in visited and new_score <= end_score:
#             visited.add(((row, col), (new_row, new_col)))
#             heapq.heappush(queue, (new_score, new_row, new_col, new_dir, new_path))

# print(len(tiles))

# end_moves = end_score % 1000
# end_turns = end_score // 1000

# # STEP 1: Nodify the map
# # nodify start, end and any place where direction can be changed (not reversed)
# nodes = {}
# visited = {(start_row, start_col)}
# queue = [(start_row, start_col)]
# for row, col in queue:
#     nodes[(row, col)] = {}

#     for dir in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
#         new_row, new_col = row, col
#         while data[new_row][new_col] != '#':
#             new_row += dir[0]
#             new_col += dir[1]

#             # If we are moving up or down, check if we can go left or right
#             # if so, this is a new node to explore
#             if dir in [(-1, 0), (1, 0)]:
#                 if data[new_row][new_col+1] != '#' or data[new_row][new_col-1] != '#' or (new_row, new_col) == (end_row, end_col):
#                     if (new_row, new_col) not in visited:
#                         queue.append((new_row, new_col))
#                         visited.add((new_row, new_col))
#                     nodes[(row, col)][dir] = (new_row, new_col)
#                     break
#             else:
#                 # Same thing but for moving left or right
#                 if data[new_row+1][new_col] != '#' or data[new_row-1][new_col] != '#' or (new_row, new_col) == (end_row, end_col):
#                     if (new_row, new_col) not in visited:
#                         queue.append((new_row, new_col))
#                         visited.add((new_row, new_col))
#                     nodes[(row, col)][dir] = (new_row, new_col)
#                     break
# print(len(nodes))
# # STEP 2: Go through every path in the map in a dijkstra's way
# # this will find every best path in terms of nodes
# visited = set()
# queue = [(0, (start_row, start_col), (0, 1), {(start_row, start_col)}, ((start_row, start_col),))]
# best_paths = []
# while queue:
#     score, node, dir, visited, path = heapq.heappop(queue)

#     if node == (end_row, end_col):
#         best_paths.append(path)
#         visited.add(path)
#         print(path)
#         continue

#     for new_dir in nodes[node]:
#         new_node = nodes[node][new_dir]
#         new_score = score + abs(node[0] - new_node[0]) + abs(node[1] - new_node[1])
#         if new_dir != dir:
#             new_score += 1000
#         new_visited = visited | {new_node}
#         new_path = path + (new_node,)
        
#         if new_node not in visited and new_score <= end_score:
#             heapq.heappush(queue, (new_score, new_node, new_dir, new_visited, new_path))

# queue = [(0, (start_row, start_col), (0, 1), {(start_row, start_col)}, ((start_row, start_col),))]
# best_paths = []
# for score, node, dir, visited, path in queue:
#     if node == (end_row, end_col):
#         best_paths.append(path)
#         print(path)
#         continue

#     for new_dir in nodes[node]:
#         new_node = nodes[node][new_dir]
#         new_score = score + abs(node[0] - new_node[0]) + abs(node[1] - new_node[1])
#         if new_dir != dir:
#             new_score += 1000
#         new_visited = visited | {new_node}
#         new_path = path + (new_node,)
        
#         if new_node not in visited and new_score % 1000 <= end_moves and new_score // 1000 <= end_turns:
#             queue.append((new_score, new_node, new_dir, new_visited, new_path))

# print(len(best_paths))
# print(nodes[(13, 1)])

                    

# good_tiles = set()
# queue = [(0, 0, start_row, start_col, (0, 1), {(start_row, start_col)})]
# best_moves = 0
# for turns, moves, row, col, dir, visited in queue:
#     if moves > best_moves:
#         best_moves = moves
#         print(best_moves, end_moves)

#     if moves > end_moves:
#         break
#     if turns > end_turns:
#         continue

#     if (row, col) == (end_row, end_col):
#         for tile in visited:
#             good_tiles.add(tile)
#         continue

#     for new_dir in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
#         new_row, new_col = row + new_dir[0], col + new_dir[1]
#         new_turns = turns
#         new_moves = moves + 1
#         if new_dir != dir:
#             new_score += 1000
#             new_turns += 1
#         new_visited = visited | {(new_row, new_col)}
        
#         if 0 <= new_row < len(data) and 0 <= new_col < len(data[0]) and data[row][col] != '#' and (new_row, new_col) not in visited:
#             queue.append((new_turns, new_moves, new_row, new_col, new_dir, new_visited))
    
# print(len(good_tiles))
            