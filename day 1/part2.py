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
for num in left:
    total += num * right.count(num)

print(total)