import collections

A = collections.Counter([1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7])
print(A)
# Counter({3: 4, 1: 2, 2: 2, 4: 1, 5: 1, 6: 1, 7: 1})
print(A.most_common(1))
# [(3, 4)]
print(A.most_common(3))
# [(3, 4), (1, 2), (2, 2)]
