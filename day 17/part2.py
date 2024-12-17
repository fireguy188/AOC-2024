from aocd import get_data
data = get_data(day=17, year=2024)

# data = '''Register A: 2024
# Register B: 0
# Register C: 0

# Program: 0,3,5,4,3,0'''

# 2,4,1,1,7,5,4,6,0,3,1,4,5,5,3,0              A=a, B=b, C=c
# (2,4) set reg B to reg A % 8                 A=a, B=a%8, C=c
# (1,1) set reg B to reg B xor 1               A=a, B=a%8 xor 1, C=c
# (7,5) set reg C to reg A // (2**reg B)       A=a, B=a%8 xor 1, C=a // 2**(a%8 xor 1)
# (4,6) set reg B to reg B xor reg C           A=a, B=(a%8 xor 1) xor (a // 2**(a%8 xor 1)), C=a // 2**(a%8 xor 1)
# (0,3) set reg A to reg A // 8                A=a//8, B=(a%8 xor 1) xor (a // 2**(a%8 xor 1)), C=a // 2**(a%8 xor 1)
# (1,4) set reg B to reg B xor 4               A=a//8, B=(a%8 xor 1) xor (a // 2**(a%8 xor 1)) xor 4, C=a // 2**(a%8 xor 1)
# (5,5) output reg B % 8                       output ((a%8 xor 1) xor (a // 2**(a%8 xor 1)) xor 4) % 8
# (3,0) go to beginning if A != 0              if a//8 > 0 go to beginning with reg A being a//8


# Lets look at the last number to determine the first 3 digits of a
# at this point, a is only 3 bits
# ((a xor 1) xor (a // 2**(a xor 1)) xor 4) % 8 = 0
# so first 3 digits are 101 (5)
# repeat this process for digits from right to left

reg_data, prog_data = data.strip().split('\n\n')

program = [int(x) for x in prog_data.split(': ')[1].split(',')]

queue = [('', program[::-1])]
for ans, digits in queue:
    if digits == []:
        break

    for bits3 in range(8):
        a = int(ans + bin(bits3)[2:].zfill(3), 2)
        if ((bits3 ^ 1) ^ (a // 2**(bits3 ^ 1)) ^ 4) % 8 == digits[0]:
            new_ans = ans + bin(bits3)[2:].zfill(3)
            queue.append((new_ans, digits[1:]))

print(int(ans, 2))
