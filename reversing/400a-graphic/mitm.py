vals = [0xdeadbeef,0xcafebabe,0xdeadbabe,0x8badf00d,0xb16b00b5,0xcafed00d,0xdeadc0de,0xdeadfa11,0xdefec8ed,0xdeadfeed,0xfee1dead,0xfaceb00b,0xfacefeed,0x000ff1ce,0x12345678,0x743029ab,0xdeed1234,0x00000000,0x11111111,0x11111112,0x11111113,0x42424242]

start = 0xdeadbeef
target = 0x764c648c

group1 = vals[:11]
group2 = vals[11:]
print(len(group1), len(group2))

def recur(begin, rest):
    ret = []
    if not rest:
        return [begin]

    for i in rest[0]:
        ret += recur(begin + [i], rest[1:])
    return ret

def all_possible(l):
    l = list(zip([0x0] * len(l), l))
    return recur([], l)

def xor_all(l, begin=0x0):
    for i in l:
        begin ^= i
    return begin

group1_xors = {}
group2_xors = {}

for i in all_possible(group1):
    group1_xors[xor_all(i, start)] = i

for i in all_possible(group2):
    group2_xors[xor_all(i, target)] = i

intersect = set(group1_xors.keys()) & set(group2_xors.keys())
print(intersect)
sol = intersect.pop()
print(hex(sol))

valsol = group1_xors[sol] + group2_xors[sol]
valsol = [i for i in valsol if i != 0]

print(hex(xor_all(valsol, start)))
print(list(map(hex, valsol)))
