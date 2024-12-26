from aocd import get_data
data = get_data(day=24, year=2024)

# data = '''x00: 1
# x01: 1
# x02: 1
# y00: 0
# y01: 1
# y02: 0

# x00 AND y00 -> z00
# x01 XOR y01 -> z01
# x02 OR y02 -> z02'''

values = {}

initial_values, gates = data.strip().split('\n\n')
for line in initial_values.split('\n'):
    name, value = line.split(': ')
    values[name] = int(value)

gates = [line.split(' -> ') for line in gates.split('\n')]
gates = {gate[1]: gate[0].split() for gate in gates}

# # c0 = 0
# # ci = (xi-1 AND yi-1) OR ((xi-1 XOR yi-1) AND ci-1)
# # zi = (xi XOR yi) XOR ci

# # z10 = c10
# # z17 = 

# x00 XOR y00 -> z00
# x00 AND y00 -> c1

# x01 XOR y01 -> p1
# p1 XOR c1 -> z01
# x01 AND y01 -> q1
# p1 AND c1 -> r1
# q1 OR r1 -> c2

# x02 XOR y02 -> p2
# p2 XOR c2 -> z02
# x02 AND y02 -> q2
# p2 AND c2 -> r2
# q2 OR r2 -> c3

# ...

# x44 XOR y44 -> p44
# p44 XOR c44 -> z44
# x44 AND y44 -> q44
# p44 AND c44 -> r44
# q44 OR r44 -> z45

my_gates = {'z00': ['x00', 'XOR', 'y00'], 'c1': ['x00', 'AND', 'y00']}
for i in range(1, 44):
    my_gates['p' + str(i).zfill(2)] = ['x' + str(i).zfill(2), 'XOR', 'y' + str(i).zfill(2)]


# Will be a mapping of their wire names to my wire names
max_num = len(values) // 2
mappings = {}

no_touch = ['z10', 'ggn', 'jcb', 'ndw', 'z32', 'grm', 'z39', 'twr']
mappings['z10'] = 'z10'
mappings['ggn'] = 'c11'

mappings['jcb'] = 'q17'
mappings['ndw'] = 'p17'

mappings['z32'] = 'z32'
mappings['grm'] = 'r32'

mappings['z39'] = 'z39'
mappings['twr'] = 'q39'

# Handle z00 case
for out_wire in gates:
    if out_wire in no_touch:
        continue

    gate = gates[out_wire]

    if gate == ['x00', 'XOR', 'y00'] or gate == ['y00', 'XOR', 'x00']:
        mappings[out_wire] = 'z00'
    elif gate == ['x00', 'AND', 'y00'] or gate == ['y00', 'AND', 'x00']:
        mappings[out_wire] = 'c01'

# Handle ps and qs
for out_wire in gates:
    if out_wire in no_touch:
        continue

    gate = gates[out_wire]

    if gate == ['x00', 'XOR', 'y00'] or gate == ['y00', 'XOR', 'x00'] or gate == ['x00', 'AND', 'y00'] or gate == ['y00', 'AND', 'x00']:
        continue
    
    if gate[0][0] not in 'xy':
        continue
    i = int(gate[0][1:])

    checks = [['x' + str(i).zfill(2), 'XOR', 'y' + str(i).zfill(2)], ['y' + str(i).zfill(2), 'XOR', 'x' + str(i).zfill(2)]]
    if gate in checks:
        mappings[out_wire] = 'p' + str(i).zfill(2)
    
    checks = [['x' + str(i).zfill(2), 'AND', 'y' + str(i).zfill(2)], ['y' + str(i).zfill(2), 'AND', 'x' + str(i).zfill(2)]]
    if gate in checks:
        mappings[out_wire] = 'q' + str(i).zfill(2)

# Handle rs and cs and zs
for i in range(1, max_num):
    for out_wire in gates:
        if out_wire in no_touch:
            continue

        gate = gates[out_wire]
        
        if gate[0] not in mappings or gate[2] not in mappings:
            continue

        mapped_gate = [mappings[gate[0]], gate[1], mappings[gate[2]]]

        if mapped_gate == ['p' + str(i).zfill(2), 'AND', 'c' + str(i).zfill(2)] or mapped_gate == ['c' + str(i).zfill(2), 'AND', 'p' + str(i).zfill(2)]:
            mappings[out_wire] = 'r' + str(i).zfill(2)
        if mapped_gate == ['p' + str(i).zfill(2), 'XOR', 'c' + str(i).zfill(2)] or mapped_gate == ['c' + str(i).zfill(2), 'XOR', 'p' + str(i).zfill(2)]:
            mappings[out_wire] = 'z' + str(i).zfill(2)
    
    for out_wire in gates:
        if out_wire in no_touch:
            continue

        gate = gates[out_wire]
        
        if gate[0] not in mappings or gate[2] not in mappings:
            continue

        mapped_gate = [mappings[gate[0]], gate[1], mappings[gate[2]]]

        if mapped_gate == ['q' + str(i).zfill(2), 'OR', 'r' + str(i).zfill(2)] or mapped_gate == ['r' + str(i).zfill(2), 'OR', 'q' + str(i).zfill(2)]:
            mappings[out_wire] = 'c' + str(i+1).zfill(2)

print(mappings)