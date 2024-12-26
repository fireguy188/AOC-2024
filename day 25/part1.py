from aocd import get_data
data = get_data(day=25, year=2024)

# data = '''#####
# .####
# .####
# .####
# .#.#.
# .#...
# .....

# #####
# ##.##
# .#.##
# ...##
# ...#.
# ...#.
# .....

# .....
# #....
# #....
# #...#
# #.#.#
# #.###
# #####

# .....
# .....
# #.#..
# ###..
# ###.#
# ###.#
# #####

# .....
# .....
# .....
# #....
# #.#..
# #.#.#
# #####'''

data = data.strip().split('\n\n')

locks, keys = [], []

for schematic in data:
    schematic = schematic.split('\n')

    if schematic[0] == '#####':
        heights = []
        for col in range(5):
            row = 0
            while row+1 < len(schematic) and schematic[row+1][col] == '#':
                row += 1
            heights.append(row)
            
        locks.append(heights)
    else:
        heights = []
        for col in range(5):
            row = len(schematic)-1
            while row-1 >= 0 and schematic[row-1][col] == '#':
                row -= 1
            heights.append(len(schematic)-row-1)

        keys.append(heights)

total = 0
for lock in locks:
    for key in keys:
        for col in range(5):
            if lock[col] + key[col] > 5:
                break
        else:
            total += 1

print(total)