from aocd import get_data
data = get_data(day=18, year=2024)

# data = '''5,4
# 4,2
# 4,5
# 3,0
# 2,1
# 6,3
# 2,4
# 1,5
# 0,6
# 3,3
# 2,6
# 5,1
# 1,2
# 5,5
# 2,5
# 6,5
# 1,4
# 0,4
# 6,4
# 1,1
# 6,1
# 1,0
# 0,5
# 1,6
# 2,0'''

data = data.strip().split('\n')
width = 70+1

corrupted = set()
for byte in range(len(data)):
    col, row = data[byte].split(',')
    corrupted.add((int(row), int(col)))

    visited = {(0, 0)}
    queue = [(0, 0, 0)]
    for row, col, moves in queue:
        if (row, col) == (width-1, width-1):
            break

        for change in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + change[0], col + change[1]

            if (new_row, new_col) in corrupted:
                continue

            if 0 <= new_row < width and 0 <= new_col < width and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, moves+1))
    else:
        print(data[byte])
        break

# for row in range(width):
#     print_row = ''
#     for col in range(width):
#         if (row, col) in corrupted:
#             print_row += '#'
#         else:
#             print_row += '.'
#     print(print_row)