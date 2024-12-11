from aocd import get_data
data = get_data(day=11, year=2024)

stones = [int(x) for x in data.strip().split()]

for blink in range(25):
    new_stones = []
    for stone in stones:
        length = len(str(stone))
        if stone == 0:
            new_stones.append(1)
        elif length % 2 == 0:
            new_stones.append(int(str(stone)[:length//2]))
            new_stones.append(int(str(stone)[length//2:]))
        else:
            new_stones.append(stone*2024)
    stones = new_stones

print(len(stones))