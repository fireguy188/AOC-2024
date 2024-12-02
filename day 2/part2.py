from aocd import get_data
data = get_data(day=2, year=2024)

def check(line, dif):
    removed = False
    i = 1
    while i < len(line):
        if not (1 <= dif(line[i], line[i-1]) <= 3):
            # Either i-1 or i shouldn't be here
            if removed:
                return False

            # removing i-1 means we need to check i-2 works with i, and i works with i+1, then we add 2 to i
            # removing i means we need to check i-1 works with i+1, and then we add 2 to i
            # adding 2 gets done because of the i+1 outside the if

            # removing i-1
            if (i == 1 or 1 <= dif(line[i], line[i-2]) <= 3) and (i == len(line)-1 or 1 <= dif(line[i+1], line[i]) <= 3):
                i += 1
            # removing i
            elif (i == len(line)-1 or 1 <= dif(line[i+1], line[i-1]) <= 3):
                i += 1
            else:
                # can't remove either
                return False

            removed = True
        
        i += 1

    return True


total = 0
for line in data.split('\n'):
    line = [int(x) for x in line.split()]

    # Check with increasing and decreasing
    if check(line, lambda x, y: x - y) or check(line, lambda x, y: y - x):
        total += 1

print(total)




### BAD CODE ###
# def is_safe(line):
#     # Try increasing
#     for i in range(1, len(line)):
#         if line[i-1] >= line[i]:
#             break

#         if not (1 <= line[i] - line[i-1] <= 3):
#             break
#     else:
#         return True
    
#     # Try decreasing
#     for i in range(1, len(line)):
#         if line[i-1] <= line[i]:
#             break

#         if not (1 <= line[i-1] - line[i] <= 3):
#             break
#     else:
#         return True
    
#     return False

# total = 0
# for line in data.split('\n'):
#     line = [int(x) for x in line.split()]

#     for i in range(len(line)):
#         if is_safe(line[:i] + line[i+1:]):
#             total += 1
#             break

# def dif(n1, n2, first):
#     if first == 0:
#         return n1 - n2
#     return n2 - n1