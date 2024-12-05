from aocd import get_data
data = get_data(day=4, year=2024)
# data = '''.M.S......
# ..A..MSMS.
# .M.S.MAA..
# ..A.ASMSM.
# .M.S.M....
# ..........
# S.S.S.S.S.
# .A.A.A.A..
# M.M.M.M.M.
# .......S.M
# ........A.
# .......S.M
# '''

data = data.split('\n')
total = 0

# Find diagonal
for r in range(len(data)-2):
    for c in range(len(data[r])-2):
        if data[r+1][c+1] == 'A':
            if data[r][c] != data[r+2][c+2] and data[r][c+2] != data[r+2][c]:
                letters = [data[r][c], data[r+2][c+2], data[r][c+2], data[r+2][c]]
                if letters.count('M') == 2 and letters.count('S') == 2:
                    total += 1

print(total)