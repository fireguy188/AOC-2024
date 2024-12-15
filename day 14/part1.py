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

occupied = {}
width, height = 101, 103
for line in data:
    pos_str, vel_str = line.split()
    pos = tuple(int(x) for x in pos_str[2:].split(','))
    vel = tuple(int(x) for x in vel_str[2:].split(','))
    
    for move in range(100):
        pos = ((pos[0] + vel[0]) % width, (pos[1] + vel[1]) % height)

    if not pos in occupied:
        occupied[pos] = 0
    occupied[pos] += 1

ul, ur, bl, br = 0, 0, 0, 0
for pos in occupied:
    if pos[0] < width // 2:
        # Left half
        if pos[1] < height // 2:
            # UL quadrant
            ul += occupied[pos]
        elif pos[1] > height // 2:
            # BL quadrant
            bl += occupied[pos]
    elif pos[0] > width // 2:
        # Right half
        if pos[1] < height // 2:
            # UR quadrant
            ur += occupied[pos]
        elif pos[1] > height // 2:
            # BR quadrant
            br += occupied[pos]

print(ul * ur * bl * br)
#print(ul, ur, bl, br)