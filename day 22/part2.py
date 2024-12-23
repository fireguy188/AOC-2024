from aocd import get_data
data = get_data(day=22, year=2024)

# data = '''1
# 2
# 3
# 2024'''

data = data.strip().split('\n')

def next_secret(secret):
    secret = (secret ^ (secret * 64)) % 16777216
    secret = (secret ^ (secret // 32)) % 16777216
    secret = (secret ^ (secret * 2048)) % 16777216

    return secret

all_seq_results = []
all_seqs = set()
for initial in data:
    seq_results = {}
    secret = int(initial)
    price = secret % 10
    changes = tuple()
    for _ in range(2000):
        secret = next_secret(secret)
        changes += (secret % 10 - price,)
        price = secret % 10

        if len(changes) > 4:
            changes = changes[1:]

        if len(changes) == 4 and changes not in seq_results:
            seq_results[changes] = price
            all_seqs.add(changes)

    all_seq_results.append(seq_results)

best = None
for changes in all_seqs:
    score = 0
    for seq_results in all_seq_results:
        score += seq_results.get(changes, 0)
    
    if best == None or score > best[0]:
        best = (score, changes)
    
print(best[0])