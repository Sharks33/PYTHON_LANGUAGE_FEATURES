# (slice(start, end, step))
a = [0, 1, 2, 3, 4, 5]
LASTTHREE = slice(-3, None)
print(LASTTHREE)
# slice(-3, None, None)
print(a[LASTTHREE])
# [3, 4, 5]
