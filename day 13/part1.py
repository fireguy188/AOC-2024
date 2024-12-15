from aocd import get_data
data = get_data(day=13, year=2024)

# data = '''Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400

# Button A: X+26, Y+66
# Button B: X+67, Y+21
# Prize: X=12748, Y=12176

# Button A: X+17, Y+86
# Button B: X+84, Y+37
# Prize: X=7870, Y=6450

# Button A: X+69, Y+23
# Button B: X+27, Y+71
# Prize: X=18641, Y=10279'''

data = data.strip().split('\n\n')

# never any - moves
total = 0
for game in data:
    game = game.strip().split('\n')

    line1 = game[0].split(': ')[1].split(', ')
    a = [int(x[2:]) for x in line1]
    line2 = game[1].split(': ')[1].split(', ')
    b = [int(x[2:]) for x in line2]
    line3 = game[2].split(': ')[1].split(', ')
    target = [int(x[2:]) for x in line3]
    
    best = float('inf')
    for a_press in range(100+1):
        for b_press in range(100+1):
            x = a_press * a[0] + b_press * b[0]
            y = a_press * a[1] + b_press * b[1]
            if target == [x, y]:
                best = min(best, a_press * 3 + b_press)
    
    if best != float('inf'):
        total += best

print(total)