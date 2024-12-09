from aocd import get_data
data = get_data(day=8, year=2024)

antennas = {}
antinodes = set()

data = data.strip().split('\n')

for row in range(len(data)):
    for col in range(len(data[row])):
        char = data[row][col]
        if char != '.':
            if not char in antennas:
                antennas[char] = []
            
            # Go through every previous antenna of the same type
            # get distance between this one and all the old ones
            # place 2 antinodes
            for (r, c) in antennas[char]:
                r_dist, c_dist = r - row, c - col
                antinodes.add((r-r_dist*2, c-c_dist*2))
                antinodes.add((row+r_dist*2, col+c_dist*2))

            antennas[char].append((row, col))

# 332 too high
total = 0
for (r, c) in antinodes:
    if 0 <= r < len(data) and 0 <= c < len(data[0]):
        total += 1
print(total)
