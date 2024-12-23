from aocd import get_data
data = get_data(day=21, year=2024)

data = '''029A
980A
179A
456A
379A'''

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

def h(state, code):
    num_robot, _, entered = state
    
    if entered == code:
        return 0
    
    return 1000000 * (len(code) - len(entered)) + numpad_distances[num_robot][code[len(entered)]]

import heapq

total = 0
for code in data:
    print(code)
    start = ('A', tuple('A' for _ in range(7)), '')
    visited = {start}
    queue = [(h(start, code), 0) + start]
    while queue:
        score, moves, num_robot, dir_robots, entered = heapq.heappop(queue)
        #print(entered)

        if entered == code:
            total += int(code[:-1]) * moves
            break

        # Move outermost robot in one of the 4 directions
        for dir in ['<', '^', '>', 'v']:
            if dir not in dirpad_moves[dir_robots[-1]]:
                continue
            
            new_dir_robots = dir_robots[:-1] + (dirpad_moves[dir_robots[-1]][dir],)
            new_state = (num_robot, new_dir_robots, entered)
            if new_state not in visited:
                visited.add(new_state)
                heapq.heappush(queue, (moves+1+h(new_state, code), moves+1) + new_state)
        
        # Try making outermost robot push a button
        new_num_robot = num_robot
        new_dir_robots = dir_robots
        new_entered = entered

        cur_dir_robot = len(dir_robots)-1
        while cur_dir_robot >= 0 and dir_robots[cur_dir_robot] == 'A':
            cur_dir_robot -= 1

        if cur_dir_robot == -1:
            # All direction robots are pointing at the A button
            new_entered = entered + num_robot
            if not code.startswith(new_entered):
                continue
        elif cur_dir_robot == 0:
            # Final direction robot is moving the hand of the numpad robot
            if dir_robots[0] not in numpad_moves[num_robot]:
                continue
            new_num_robot = numpad_moves[num_robot][dir_robots[0]]
        else:
            # A direction robot is moving the hand of another direction robot
            if dir_robots[cur_dir_robot] not in dirpad_moves[dir_robots[cur_dir_robot-1]]:
                continue
            new_dir_robots = dir_robots[:cur_dir_robot-1] + (dirpad_moves[dir_robots[cur_dir_robot-1]][dir_robots[cur_dir_robot]],) + dir_robots[cur_dir_robot:]
        
        new_state = (new_num_robot, new_dir_robots, new_entered)
        if new_state not in visited:
            visited.add(new_state)
            heapq.heappush(queue, (moves+1+h(new_state, code), moves+1) + new_state)

print(total)