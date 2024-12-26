from aocd import get_data
data = get_data(day=24, year=2024)

# data = '''x00: 1
# x01: 0
# x02: 1
# x03: 1
# x04: 0
# y00: 1
# y01: 1
# y02: 1
# y03: 1
# y04: 1

# ntg XOR fgs -> mjb
# y02 OR x01 -> tnw
# kwq OR kpj -> z05
# x00 OR x03 -> fst
# tgd XOR rvg -> z01
# vdt OR tnw -> bfw
# bfw AND frj -> z10
# ffh OR nrd -> bqk
# y00 AND y03 -> djm
# y03 OR y00 -> psh
# bqk OR frj -> z08
# tnw OR fst -> frj
# gnj AND tgd -> z11
# bfw XOR mjb -> z00
# x03 OR x00 -> vdt
# gnj AND wpb -> z02
# x04 AND y00 -> kjc
# djm OR pbm -> qhw
# nrd AND vdt -> hwm
# kjc AND fst -> rvg
# y04 OR y02 -> fgs
# y01 AND x02 -> pbm
# ntg OR kjc -> kwq
# psh XOR fgs -> tgd
# qhw XOR tgd -> z09
# pbm OR djm -> kpj
# x03 XOR y03 -> ffh
# x00 XOR y04 -> ntg
# bfw OR bqk -> z06
# nrd XOR fgs -> wpb
# frj XOR qhw -> z04
# bqk OR frj -> z07
# y03 OR x01 -> nrd
# hwm AND bqk -> z03
# tgd XOR rvg -> z12
# tnw OR pbm -> gnj'''

values = {}

initial_values, gates = data.strip().split('\n\n')
for line in initial_values.split('\n'):
    name, value = line.split(': ')
    values[name] = int(value)

gates = [line.split(' -> ') for line in gates.split('\n')]
gates = [[gate[0].split(), gate[1]] for gate in gates]

while gates:
    new_gates = []
    for rule, result in gates:
        v1, v2 = rule[0], rule[2]
        if v1 in values and v2 in values:
            if rule[1] == 'AND':
                values[result] = values[v1] & values[v2]
            elif rule[1] == 'XOR':
                values[result] = values[v1] ^ values[v2]
            elif rule[1] == 'OR':
                values[result] = values[v1] | values[v2]
        else:
            new_gates.append([rule, result])
    gates = new_gates

ans = ''
i = 0
while True:
    v = 'z' + str(i).zfill(2)

    if v not in values:
        break

    ans = str(values[v]) + ans

    i += 1

print(int(ans, 2))