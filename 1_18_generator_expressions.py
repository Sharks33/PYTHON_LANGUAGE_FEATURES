g = (x ** 2 for x in xrange(10))
print(next(g))
# 0
print(next(g))
# 1
print(next(g))
# 4
print(next(g))
# 9
print(sum(x ** 3 for x in xrange(10)))
# 2025
print(sum(x ** 3 for x in xrange(10) if x % 3 == 1))
# 408
