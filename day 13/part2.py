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
# no infinite solutions
# no negative solutions
# all above checked
total = 0
for game in data:
    game = game.strip().split('\n')

    line1 = game[0].split(': ')[1].split(', ')
    a = [int(x[2:]) for x in line1]
    line2 = game[1].split(': ')[1].split(', ')
    b = [int(x[2:]) for x in line2]
    line3 = game[2].split(': ')[1].split(', ')
    target = [int(x[2:]) + 10000000000000 for x in line3]

    # equations
    # a_presses * a[0] + b_presses * b[0] = target[0]
    # a_presses * a[1] + b_presses * b[1] = target[1]
    #
    # minimize a_presses * 3 + b_presses
    #
    # GAUSSIAN ELIMINATION
    # multiply top equation by a[1]/a[0] and subtract it from bottom equation
    # b_presses * b[1] - b_presses * b[0] * a[1] / a[0] = target[1] - target[0] * a[1] / a[0]
    # b_presses(b[1] - b[0] * a[1] / a[0]) = target[1] - target[0] * a[1] / a[0]
    # b_presses = (target[1] - target[0] * a[1] / a[0]) / (b[1] - b[0] * a[1] / a[0])

    n = a[0] * target[1] - target[0] * a[1]
    d = b[1] * a[0] - b[0] * a[1]

    if n % d == 0:
        b_presses = n // d
        a_presses = (target[0] - b_presses * b[0]) // a[0]

        x = a_presses * a[0] + b_presses * b[0]
        y = a_presses * a[1] + b_presses * b[1]
        if x == target[0] and y == target[1]:
            total += b_presses + a_presses * 3
    
print(total)