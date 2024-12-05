from aocd import get_data
data = get_data(day=5, year=2024)

# data = '''47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47'''

rules_str, checks = data.split('\n\n')

rules = {}
for rule in rules_str.split('\n'):
    p1, p2 = rule.split('|')

    if not p1 in rules:
        rules[p1] = []
    rules[p1].append(p2)

def allowed_before(p1, p2):
    return not p1 in rules.get(p2, [])

def is_safe(check):
    for i in range(len(check)-1):
        for j in range(i+1, len(check)):
            if not allowed_before(check[i], check[j]):
                return False
    
    return True

total = 0
for check in checks.split('\n'):
    check = check.split(',')

    if is_safe(check):
        total += int(check[len(check)//2])

print(total)