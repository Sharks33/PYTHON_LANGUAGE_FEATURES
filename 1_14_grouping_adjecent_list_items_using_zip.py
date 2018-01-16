a = [1, 2, 3, 4, 5, 6]

# Using iterators
group_adjacent = lambda a, k: zip(*([iter(a)] * k))
print(group_adjacent(a, 3))
# [(1, 2, 3), (4, 5, 6)]
print(group_adjacent(a, 2))
# [(1, 2), (3, 4), (5, 6)]
print(group_adjacent(a, 1))
# [(1,), (2,), (3,), (4,), (5,), (6,)]


# Using slices
from itertools import islice
group_adjacent = lambda a, k: zip(*(islice(a, i, None, k) for i in range(k)))
print(group_adjacent(a, 3))
# [(1, 2, 3), (4, 5, 6)]
print(group_adjacent(a, 2))
# [(1, 2), (3, 4), (5, 6)]
print(group_adjacent(a, 1))
# [(1,), (2,), (3,), (4,), (5,), (6,)]
