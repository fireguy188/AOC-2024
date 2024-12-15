from aocd import get_data
data = get_data(day=12, year=2024)

# data = '''RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
# VVRCCCJFFF
# VVVVCJJCFE
# VVIVCCJJEE
# VVIIICJJEE
# MIIIIIJJEE
# MIIISIJEEE
# MMMISSJEEE'''

data = data.strip().split('\n')

def explore(row, col, regions, visited):
    plot = data[row][col]
    visited.add((row, col))
    queue = [(row, col)]
    new_explorations = []
    for row, col in queue:
        adjacent = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        for new_row, new_col in adjacent:
            if (new_row, new_col) in visited:
                continue

            if 0 <= new_row < len(data) and 0 <= new_col < len(data[0]):
                if data[new_row][new_col] == plot:
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col))
                else:
                    new_explorations.append((new_row, new_col))

    regions.append(queue)

    for row, col in new_explorations:
        if (row, col) not in visited:
            explore(row, col, regions, visited)


regions = []
explore(0, 0, regions, set())

# Now we have to find area and perimeter of all regions
# area is easy, just length of a region (represented by list of coordinates)
# perimeter - have to go through each coordinate and find how many sides it doesn't have covered
total = 0
for region in regions:
    area = len(region)
    perimeter = 0
    set_region = set(region)

    for row, col in region:
        sides = 4
        adjacent = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        for new_row, new_col in adjacent:
            if (new_row, new_col) in set_region:
                sides -= 1

        perimeter += sides

    total += area * perimeter

print(total)