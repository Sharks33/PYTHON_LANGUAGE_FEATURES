import collections

last_three = collections.deque(maxlen=3)

for i in xrange(10):
    last_three.append(i)
    print ', '.join(str(x) for x in last_three)

# 0
# 0, 1
# 0, 1, 2
# 1, 2, 3
# 2, 3, 4
# 3, 4, 5
# 4, 5, 6
# 5, 6, 7
# 6, 7, 8
# 7, 8, 9
