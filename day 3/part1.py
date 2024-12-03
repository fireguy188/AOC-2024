from aocd import get_data
import re
data = get_data(day=3, year=2024)
#data = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

total = 0
for m in re.findall(r'mul\(\d{1,3},\d{1,3}\)', data):
    n1, n2 = m[4:-1].split(',')
    total += int(n1) * int(n2)

print(total)