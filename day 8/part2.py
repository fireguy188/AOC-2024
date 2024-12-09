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
            for (r, c) in antennas[char]:
                r_dist, c_dist = r - row, c - col
                antinode = (r-r_dist, c-c_dist)
                while 0 <= antinode[0] < len(data) and 0 <= antinode[1] < len(data[0]):
                    antinodes.add(antinode)
                    antinode = (antinode[0]-r_dist, antinode[1]-c_dist)
                
                antinode = (row+r_dist, col+c_dist)
                while 0 <= antinode[0] < len(data) and 0 <= antinode[1] < len(data[0]):
                    antinodes.add(antinode)
                    antinode = (antinode[0]+r_dist, antinode[1]+c_dist)

            antennas[char].append((row, col))

print(len(antinodes))
