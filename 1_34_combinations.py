import itertools

for c in itertools.combinations([1, 2, 3, 4, 5], 3):
    print(''.join(str(x) for x in c))

# 123
# 124
# 125
# 134
# 135
# 145
# 234
# 235
# 245
# 345

for c in itertools.combinations_with_replacement([1, 2, 3], 2):
    print(''.join(str(x) for x in c))

# 11
# 12
# 13
# 22
# 23
# 33
