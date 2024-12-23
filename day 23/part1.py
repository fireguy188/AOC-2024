from aocd import get_data
data = get_data(day=23, year=2024)

# data = '''kh-tc
# qp-kh
# de-cg
# ka-co
# yn-aq
# qp-ub
# cg-tb
# vc-aq
# tb-ka
# wh-tc
# yn-cg
# kh-ub
# ta-co
# de-co
# tc-td
# tb-wq
# wh-td
# ta-ka
# td-qp
# aq-cg
# wq-ub
# ub-vc
# de-ta
# wq-aq
# wq-vc
# wh-yn
# ka-de
# kh-ta
# co-tc
# wh-qp
# tb-vc
# td-yn'''

data = data.strip().split('\n')

connections = {}
for line in data:
    c1, c2 = line.split('-')

    if c1 not in connections:
        connections[c1] = []
    if c2 not in connections:
        connections[c2] = []

    connections[c1].append(c2)
    connections[c2].append(c1)

found = set()
for comp1 in connections:
    if comp1[0] != 't':
        continue
    
    for comp2 in connections[comp1]:
        for comp3 in connections[comp2]:
            if comp3 in connections[comp1]:
                found.add(tuple(sorted((comp1, comp2, comp3))))

print(len(found))
        

