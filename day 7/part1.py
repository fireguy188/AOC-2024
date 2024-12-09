from aocd import get_data
import itertools
data = get_data(day=7, year=2024)

# data = '''190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20'''

def eval_equation(result, operands, operators):
    actual_result = operands[0]
    for i in range(1, len(operands)):
        if operators[i-1] == '+':
            actual_result += operands[i]
        else:
            actual_result *= operands[i]
    
    return result == actual_result

data = data.split('\n')
total = 0
for line in data:
    result, operands = line.split(':')
    result = int(result)
    operands = [int(x) for x in operands.split()]

    operator_options = ['+*' for _ in range(len(operands)-1)]
    for operators in itertools.product(*operator_options):
        if eval_equation(result, operands, operators):
            total += result
            break
    
print(total)
    