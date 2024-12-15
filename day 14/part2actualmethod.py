from aocd import get_data
data = get_data(day=14, year=2024)

# data = '''p=0,4 v=3,-3
# p=6,3 v=-1,-3
# p=10,3 v=-1,2
# p=2,0 v=2,-1
# p=0,0 v=1,3
# p=3,0 v=-2,-2
# p=7,6 v=-1,-3
# p=3,0 v=-1,-2
# p=9,3 v=2,3
# p=7,3 v=-1,2
# p=2,4 v=2,-3
# p=9,5 v=-3,-3'''

data = data.strip().split('\n')

width, height = 101, 103
robots = []
for line in data:
    pos_str, vel_str = line.split()
    pos = tuple(int(x) for x in pos_str[2:].split(','))
    vel = tuple(int(x) for x in vel_str[2:].split(','))

    robots.append((pos, vel))

def print_robots(robots):
    grid = [['.' for _ in range(width)] for _ in range(height)]
    for pos, _ in robots:
        grid[pos[1]][pos[0]] = 'R'
    
    for row in grid:
        print(''.join(row))
    print()
    

moves = 0
while True:
    avg_pos = (0, 0)
    for r in range(len(robots)):
        pos, vel = robots[r]
        new_pos = ((pos[0] + vel[0]) % width, (pos[1] + vel[1]) % height)
        robots[r] = (new_pos, vel)

        avg_pos = (avg_pos[0]+new_pos[0], avg_pos[1]+new_pos[1])
    
    avg_pos = (avg_pos[0]/len(robots), avg_pos[1]/len(robots))

    variance = 0
    for pos, _ in robots:
        variance += (pos[0] - avg_pos[0])**2 + (pos[1] - avg_pos[1])**2
    
    moves += 1

    if variance < 500000:
        print(f'{moves} moves:')
        print_robots(robots)
        break

    