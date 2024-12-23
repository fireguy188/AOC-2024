from aocd import get_data
data = get_data(day=21, year=2024)

# data = '''029A
# 980A
# 179A
# 456A
# 379A'''

numpad = [['7', '8', '9'],
          ['4', '5', '6'],
          ['1', '2', '3'],
          [None, '0', 'A']]

dirpad = [[None, '^', 'A'],
          ['<', 'v', '>']]

data = data.strip().split('\n')

# STEP 1: Get all best movement paths between any 2 symbols. e.g '>' to '<' is <<A

numpad_moves = {}
for row in range(len(numpad)):
    for col in range(len(numpad[0])):
        if numpad[row][col] == None:
            continue

        numpad_moves[numpad[row][col]] = {}
        for row2 in range(len(numpad)):
            for col2 in range(len(numpad[0])):
                if numpad[row2][col2] == None:
                    continue
                
                move = ''
                if row > row2:
                    move += '^'*abs(row-row2)
                    if col > col2:
                        move += '<'*abs(col-col2)
                    elif col < col2:
                        move += '>'*abs(col-col2)
                elif row < row2:
                    if col > col2:
                        move += '<'*abs(col-col2)
                    elif col < col2:
                        move += '>'*abs(col-col2)
                    move += 'v'*abs(row-row2)
                else:
                    if col > col2:
                        move += '<'*abs(col-col2)
                    elif col < col2:
                        move += '>'*abs(col-col2)

                numpad_moves[numpad[row][col]][numpad[row2][col2]] = move + 'A'

dirpad_moves = {}
for row in range(len(dirpad)):
    for col in range(len(dirpad[0])):
        if dirpad[row][col] == None:
            continue

        dirpad_moves[dirpad[row][col]] = {}
        for row2 in range(len(dirpad)):
            for col2 in range(len(dirpad[0])):
                if dirpad[row2][col2] == None:
                    continue
                
                move = ''
                if row > row2:
                    if col > col2:
                        move += '<'*abs(col-col2)
                    elif col < col2:
                        move += '>'*abs(col-col2)
                    move += '^'*abs(row-row2)
                elif row < row2:
                    move += 'v'*abs(row-row2)
                    if col > col2:
                        move += '<'*abs(col-col2)
                    elif col < col2:
                        move += '>'*abs(col-col2)
                else:
                    if col > col2:
                        move += '<'*abs(col-col2)
                    elif col < col2:
                        move += '>'*abs(col-col2)

                dirpad_moves[dirpad[row][col]][dirpad[row2][col2]] = move + 'A'

# STEP 2: Get the moves required for the first digit in the code. e.g code 029A, to get 0 moves are <A

# STEP 3: Go through each move in the moves found for this code digit, look at the previous move and use
# step 1 to calculate the move required. e.g <A becomes (v<<A)(>>^A)

import functools

@functools.cache
def get_length(instructions, level):
    if level == 0:
        return len(instructions)
    
    prev_digit = 'A'
    total = 0
    for digit in instructions:
        options = [dirpad_moves[prev_digit][digit], dirpad_moves[prev_digit][digit][:-1][::-1] + 'A']
        best = float('inf')
        for option in options:
            if prev_digit in '<' and digit in '^A' and option[0] == '^':
                continue
            if prev_digit in '^A' and digit in '<' and option[0] == '<':
                continue

            best = min(best, get_length(option, level-1))
        
        total += best

        prev_digit = digit

    return total


ans = 0
for code in data:
    total = 0
    prev_digit = 'A'
    for digit in code:
        # ^^<< could be worse than <<^^
        options = [numpad_moves[prev_digit][digit], numpad_moves[prev_digit][digit][:-1][::-1] + 'A']
        best = float('inf')
        for option in options:
            if prev_digit in '0A' and digit in '147' and option[0] == '<':
                continue
            if prev_digit in '147' and digit in '0A' and option[0] == 'v':
                continue

            best = min(best, get_length(option, 25))

        total += best
        prev_digit = digit
    
    ans += total * int(code[:-1])

print(ans)

# STEP 4: Go through each bracketed move and run a recursive function to generate the length of instructions for it
# the speedup will be because the bracketed moves will appear multiple times. There's only 5*5 = 25 possible bracketed movements

