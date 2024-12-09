from aocd import get_data
data = get_data(day=9, year=2024)

#data = '2333133121414131402'

actual_data = []
block = True
for d in range(len(data)):
    if block:
        for _ in range(int(data[d])):
            actual_data.append(d//2)
    else:
        for _ in range(int(data[d])):
            actual_data.append('.')
    
    block = not block

#print(''.join([str(x) for x in actual_data]))
left_free = 0
right_occupied = len(actual_data)-1
while left_free < right_occupied:
    if actual_data[left_free] != '.':
        left_free += 1
        continue

    if actual_data[right_occupied] == '.':
        right_occupied -= 1
        continue
    
    actual_data[left_free], actual_data[right_occupied] = actual_data[right_occupied], actual_data[left_free]
    left_free += 1
    right_occupied -= 1

total = 0
for d in range(len(actual_data)):
    if actual_data[d] == '.':
        break

    total += actual_data[d] * int(d)

print(total)