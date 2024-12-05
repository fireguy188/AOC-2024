from aocd import get_data
data = get_data(day=4, year=2024)
# data = '''MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX'''

data = data.split('\n')
total = 0

# Find horizontal
for r in range(len(data)):
    for c in range(len(data[r])-3):
        if data[r][c:c+4] == 'XMAS':
            total += 1
        if data[r][c:c+4] == 'SAMX':
            total += 1

# Find vertical
for c in range(len(data[0])):
    for r in range(len(data)-3):
        word = ''.join([data[row][c] for row in range(r, r+4)])
        if word == 'XMAS':
            total += 1
        if word == 'SAMX':
            total += 1

# Find diagonal
for r in range(len(data)-3):
    # down and right
    for c in range(len(data[r])-3):
        word = ''.join([data[r+i][c+i] for i in range(4)])
        if word == 'XMAS':
            total += 1
        if word == 'SAMX':
            total += 1
    
    # down and left
    for c in range(3, len(data[r])):
        word = ''.join([data[r+i][c-i] for i in range(4)])
        if word == 'XMAS':
            total += 1
        if word == 'SAMX':
            total += 1

print(total)