import collections

m = dict((str(x), x) for x in range(10))
print(', '.join(m.keys()))
# 1, 0, 3, 2, 5, 4, 7, 6, 9, 8

m = collections.OrderedDict((str(x), x) for x in range(10))
print(', '.join(m.keys()))
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

m = collections.OrderedDict((str(x), x) for x in range(10, 0, -1))
print(', '.join(m.keys()))
# 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
