from aocd import get_data
data = get_data(day=11, year=2024)

data = [int(x) for x in data.strip().split()]

def evolve_stone(stone):
    length = len(str(stone))
    if stone == 0:
        return (1,)
    elif length % 2 == 0:
        stone1, stone2 = int(str(stone)[:length//2]), int(str(stone)[length//2:])
        return (stone1, stone2)
    else:
        return (stone*2024,)

import time

start = time.time()
stones = {}
for stone in data:
    if not stone in stones:
        stones[stone] = 0
    stones[stone] += 1

for blink in range(75):
    new_stones = {}
    for stone in stones:
        for new_stone in evolve_stone(stone):
            if not new_stone in new_stones:
                new_stones[new_stone] = 0
            new_stones[new_stone] += stones.get(stone, 0)
    stones = new_stones

print(sum(stones.values()))

print(time.time()-start)