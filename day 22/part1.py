from aocd import get_data
data = get_data(day=22, year=2024)

# data = '''1
# 10
# 100
# 2024'''

data = data.strip().split('\n')

def next_secret(secret):
    secret = (secret ^ (secret * 64)) % 16777216
    secret = (secret ^ (secret // 32)) % 16777216
    secret = (secret ^ (secret * 2048)) % 16777216

    return secret

total = 0
for initial in data:
    secret = int(initial)
    for _ in range(2000):
        secret = next_secret(secret)
    total += secret

print(total)