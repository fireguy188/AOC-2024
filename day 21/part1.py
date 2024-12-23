from aocd import get_data
data = get_data(day=21, year=2024)

# data = '''029A
# 980A
# 179A
# 456A
# 379A'''

# directions = {'^': {'^': 0, '>': 2, 'v': 1, '<': 2, 'A': 1},
#               '>': {'^': 2, '>': 0, 'v': 1, '<': 2, 'A': 1},
#               'v': {'^': 1, '>': 1, 'v': 0, '<': 1, 'A': 2},
#               '<': {'^': 2, '>': 2, 'v': 1, '<': 0, 'A': 3},
#               'A': {'^': 1, '>': 1, 'v': 2, '<': 3, 'A': 0}}

def get_distances(pad):
    distances = {}
    for row in range(len(pad)):
        for col in range(len(pad[0])):
            if pad[row][col] == None:
                continue

            distances[pad[row][col]] = {}
            for row2 in range(len(pad)):
                for col2 in range(len(pad[0])):
                    if pad[row2][col2] == None:
                        continue

                    distances[pad[row][col]][pad[row2][col2]] = abs(row-row2) + abs(col-col2)
    
    return distances

def get_moves(pad):
    moves = {}
    for row in range(len(pad)):
        for col in range(len(pad[0])):
            if pad[row][col] == None:
                continue

            moves[pad[row][col]] = {}
            
            if col > 0 and pad[row][col-1]:
                moves[pad[row][col]]['<'] = pad[row][col-1]
            if row > 0 and pad[row-1][col]:
                moves[pad[row][col]]['^'] = pad[row-1][col]
            if col < len(pad[0])-1 and pad[row][col+1]:
                moves[pad[row][col]]['>'] = pad[row][col+1]
            if row < len(pad)-1 and pad[row+1][col]:
                moves[pad[row][col]]['v'] = pad[row+1][col]

    return moves

numpad = [['7', '8', '9'],
          ['4', '5', '6'],
          ['1', '2', '3'],
          [None, '0', 'A']]

dirpad = [[None, '^', 'A'],
          ['<', 'v', '>']]

numpad_distances = get_distances(numpad)
dirpad_distances = get_distances(dirpad)

numpad_moves = get_moves(numpad)
dirpad_moves = get_moves(dirpad)

data = data.strip().split('\n')

total = 0
for code in data:
    visited = {('A', 'A', 'A', '')}
    queue = [('A', 'A', 'A', '', 0)]
    for num_robot, dir_robot1, dir_robot2, entered, moves in queue:
        if entered == code:
            total += int(code[:-1]) * moves
            break

        # Move outermost robot in one of the 4 directions
        for dir in ['<', '^', '>', 'v']:
            if dir not in dirpad_moves[dir_robot2]:
                continue

            new_dir_robot2 = dirpad_moves[dir_robot2][dir]
            if (num_robot, dir_robot1, new_dir_robot2, entered) not in visited:
                visited.add((num_robot, dir_robot1, new_dir_robot2, entered))
                queue.append((num_robot, dir_robot1, new_dir_robot2, entered, moves+1))
        
        # Try making outermost robot push a button
        new_num_robot = num_robot
        new_dir_robot1 = dir_robot1
        new_dir_robot2 = dir_robot2
        new_entered = entered
        if dir_robot2 != 'A':
            if dir_robot2 not in dirpad_moves[dir_robot1]:
                continue
            new_dir_robot1 = dirpad_moves[dir_robot1][dir_robot2]
        else:
            if dir_robot1 != 'A':
                if dir_robot1 not in numpad_moves[num_robot]:
                    continue
                new_num_robot = numpad_moves[num_robot][dir_robot1]
            else:
                new_entered = entered + num_robot
                if not code.startswith(new_entered):
                    continue
        
        if (new_num_robot, new_dir_robot1, new_dir_robot2, new_entered) not in visited:
            visited.add((new_num_robot, new_dir_robot1, new_dir_robot2, new_entered))
            queue.append((new_num_robot, new_dir_robot1, new_dir_robot2, new_entered, moves+1))

print(total)