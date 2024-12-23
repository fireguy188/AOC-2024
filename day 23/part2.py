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
        connections[c1] = set()
    if c2 not in connections:
        connections[c2] = set()

    connections[c1].add(c2)
    connections[c2].add(c1)


def explore(comp_list, available_comps, T):
    state = tuple(sorted(comp_list))

    if state in T:
        return T[state]

    best = comp_list
    for other_comp in available_comps:
        new_available_comps = available_comps.intersection(connections[other_comp])
        new_comp_list = comp_list + (other_comp,)

        if len(new_available_comps) + len(new_comp_list) <= len(best):
            continue
        
        result = explore(new_comp_list, new_available_comps, T)
        if len(result) > len(best):
            best = result

    T[state] = best
    return best

import time

start = time.time()
ans = explore(tuple(), set(connections.keys()), {})
print(time.time()-start)

print(','.join(sorted(ans)))
        

