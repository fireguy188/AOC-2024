from aocd import get_data
data = get_data(day=2, year=2024)

total = 0
for line in data.split('\n'):
    line = [int(x) for x in line.split()]
    if line[0] < line[1]:
        increasing = True
    elif line[0] > line[1]:
        increasing = False
    else:
        continue

    for i in range(1, len(line)):
        if increasing and line[i-1] >= line[i]:
            break

        if not increasing and line[i-1] <= line[i]:
            break
        
        if not (1 <= abs(line[i] - line[i-1]) <= 3):
            break
    else:
        total += 1

print(total)
