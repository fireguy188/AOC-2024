from aocd import get_data
data = get_data(day=9, year=2024)

#data = '2333133121414131402'

# Will store ranges (inclusive, exclusive)
block_locations = []
free_locations = []

actual_data = []
block = True
index = 0
for d in range(len(data)):
    if block:
        block_locations.append((index, index+int(data[d])))
        for _ in range(int(data[d])):
            actual_data.append(d//2)
    else:
        free_locations.append((index, index+int(data[d])))
        for _ in range(int(data[d])):
            actual_data.append('.')
    
    index += int(data[d])
    block = not block

# print(''.join([str(x) for x in actual_data]))
# print(block_locations)
# print(free_locations)

# Now start moving right_most data blocks left
for block_id in range(len(block_locations)-1, -1, -1):
    if block_id % 1000 == 0:
        print(block_id)
    block_space = block_locations[block_id]
    for free_index, free_space in enumerate(free_locations):
        # We aren't allowed to move the file right
        if block_space[1] <= free_space[0]:
            break

        # Not enough space to move the whole file
        block_size = block_space[1] - block_space[0]
        if free_space[1] - free_space[0] < block_size:
            continue

        block_locations[block_id] = (free_space[0], free_space[0] + block_size)
        free_locations[free_index] = (free_space[0] + block_size, free_space[1])
        break

total = 0
for block_id in range(len(block_locations)):
    block_space = block_locations[block_id]
    # This is a tiny optimisation that means nothing
    # just using n(n+1)//2 formula
    total += (block_space[1]*(block_space[1]-1)//2 - block_space[0]*(block_space[0]-1)//2) * block_id

    # This way makes more sense
    # for i in range(*block_space):
    #     total += i * block_id

print(total)