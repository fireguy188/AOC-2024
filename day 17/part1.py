from aocd import get_data
data = get_data(day=17, year=2024)

# data = '''Register A: 729
# Register B: 0
# Register C: 0

# Program: 0,1,5,4,3,0'''

registers = {}

reg_data, prog_data = data.strip().split('\n\n')

# Get initial registers
reg_data = reg_data.split('\n')
for i in range(3):
    registers['ABC'[i]] = int(reg_data[i].split(': ')[1])

program = [int(x) for x in prog_data.split(': ')[1].split(',')]

def combo(operand):
    if 0 <= operand <= 3:
        return operand
    
    if operand == 4:
        return registers['A']
    
    if operand == 5:
        return registers['B']
    
    if operand == 6:
        return registers['C']

# registers['A'] = 202972175280682 (see part 2 in action)
pc = 0
output = []
while pc < len(program):
    opcode = program[pc]
    operand = program[pc+1]

    if opcode == 0:
        registers['A'] //= (2**combo(operand))
        pc += 2
    elif opcode == 1:
        registers['B'] ^= operand
        pc += 2
    elif opcode == 2:
        registers['B'] = combo(operand) % 8
        pc += 2
    elif opcode == 3:
        if registers['A'] != 0:
            pc = operand
        else:
            pc += 2
    elif opcode == 4:
        registers['B'] ^= registers['C']
        pc += 2
    elif opcode == 5:
        output.append(combo(operand) % 8)
        pc += 2
    elif opcode == 6:
        registers['B'] = registers['A'] // (2**combo(operand))
        pc += 2
    elif opcode == 7:
        registers['C'] = registers['A'] // (2**combo(operand))
        pc += 2

print(','.join([str(x) for x in output]))