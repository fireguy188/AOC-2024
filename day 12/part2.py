from aocd import get_data
data = get_data(day=12, year=2024)

# data = '''AAAAAA
# AAABBA
# AAABBA
# ABBAAA
# ABBAAA
# AAAAAA'''

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
total = 0
for region in regions:
    area = len(region)
    perimeter = 0
    set_region = set(region)

    # Start by looking at horizontal edges
    # above and below represent if there is currently an edge above or below
    region.sort()
    cur_pos = region[0]
    above, below = False, False
    for row, col in region:
        # This point and the last point we checked are disconnected
        # they can't be part of the same side
        if cur_pos != (row, col-1):
            above, below = False, False
        cur_pos = (row, col)
        
        if not above and (row-1, col) not in set_region:
            perimeter += 1
            above = True
        elif above and (row-1, col) in set_region:
            above = False
        
        if not below and (row+1, col) not in set_region:
            perimeter += 1
            below = True
        elif below and (row+1, col) in set_region:
            below = False
    
    # now look at vertical edges
    # above and below represent if there is currently an edge left or right
    region.sort(key=lambda x: (x[1], x[0]))
    cur_pos = region[0]
    left, right = False, False
    for row, col in region:
        # This point and the last point we checked are disconnected
        # they can't be part of the same side
        if cur_pos != (row-1, col):
            left, right = False, False
        cur_pos = (row, col)
        
        if not left and (row, col-1) not in set_region:
            perimeter += 1
            left = True
        elif left and (row, col-1) in set_region:
            left = False
        
        if not right and (row, col+1) not in set_region:
            perimeter += 1
            right = True
        elif right and (row, col+1) in set_region:
            right = False

    total += area * perimeter

print(total)