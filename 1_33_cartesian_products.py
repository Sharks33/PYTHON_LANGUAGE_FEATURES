import itertools

for p in itertools.product([1, 2, 3], [4, 5]):
    print ''.join(str(x) for x in p)
# (1, 4)
# (1, 5)
# (2, 4)
# (2, 5)
# (3, 4)
# (3, 5)

for p in itertools.product([0, 1], repeat=4):
    print ''.join(str(x) for x in p)

# 0000
# 0001
# 0010
# 0011
# 0100
# 0101
# 0110
# 0111
# 1000
# 1001
# 1010
# 1011
# 1100
# 1101
# 1110
# 1111
