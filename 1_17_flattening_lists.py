import itertools

a = [[1, 2], [3, 4], [5, 6]]
print(list(itertools.chain.from_iterable(a)))
# [1, 2, 3, 4, 5, 6]

print(sum(a, []))
# [1, 2, 3, 4, 5, 6]

print([x for l in a for x in l])
# [1, 2, 3, 4, 5, 6]

a = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print([x for l1 in a for l2 in l1 for x in l2])
# [1, 2, 3, 4, 5, 6, 7, 8]

a = [1, 2, [3, 4], [[5, 6], [7, 8]]]
flatten = lambda x: [y for l in x for y in flatten(l)] if type(x) is list else [x]
print(flatten(a))
# [1, 2, 3, 4, 5, 6, 7, 8]
