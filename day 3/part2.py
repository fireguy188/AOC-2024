from aocd import get_data
import re
data = get_data(day=3, year=2024)
#data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

total = 0
enabled = True
for m in re.findall(r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)", data):
    if m == "don't()":
        enabled = False
    elif m == "do()":
        enabled = True
    elif enabled:
        n1, n2 = m[4:-1].split(',')
        total += int(n1) * int(n2)

print(total)

### COOL CODE ###
# Idea: remove everything between every pair of don't() and do() (not my idea)
# data = re.sub(r"don't\(\)(.|\n)*?do\(\)", "", data)
# then run part 1