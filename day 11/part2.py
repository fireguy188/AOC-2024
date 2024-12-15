from aocd import get_data
data = get_data(day=11, year=2024)

stones = [int(x) for x in data.strip().split()]

def evolve_stone(stone, n, T):
    if (stone, n) in T:
        return T[(stone, n)]
    
    if n == 0:
        return 1
    
    length = len(str(stone))
    if stone == 0:
        T[(stone, n)] = evolve_stone(1, n-1, T)
    elif length % 2 == 0:
        stone1, stone2 = int(str(stone)[:length//2]), int(str(stone)[length//2:])
        T[(stone, n)] = evolve_stone(stone1, n-1, T) + evolve_stone(stone2, n-1, T)
    else:
        T[(stone, n)] = evolve_stone(stone*2024, n-1, T)
    
    return T[(stone, n)]

import time
start = time.time()
T = {}
total = 0
for stone in stones:
    total += evolve_stone(stone, 75, T)
print(total)
print(time.time() - start)