import itertools

for p in itertools.permutations([1, 2, 3, 4]):
    print ''.join(str(x) for x in p)

# 1234
# 1243
# 1324
# 1342
# 1423
# 1432
# 2134
# 2143
# 2314
# 2341
# 2413
# 2431
# 3124
# 3142
# 3214
# 3241
# 3412
# 3421
# 4123
# 4132
# 4213
# 4231
# 4312
# 4321
