from aocd import get_data
data = get_data(day=1, year=2024)

left, right = [], []
for line in data.split('\n'):
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

total = 0
for i in range(len(left)):
    total += abs(right[i] - left[i])

print(total)