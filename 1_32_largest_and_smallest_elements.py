import random
import heapq

a = [random.randint(0, 100) for __ in xrange(100)]

print(heapq.nsmallest(5, a))
# [3, 3, 5, 6, 8]
print(heapq.nlargest(5, a))
# [100, 100, 99, 98, 98]
