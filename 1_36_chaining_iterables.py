import itertools

a = [1, 2, 3, 4]

for p in itertools.chain(itertools.combinations(a, 2), itertools.combinations(a, 3)):
    print(p)

# (1, 2)
# (1, 3)
# (1, 4)
# (2, 3)
# (2, 4)
# (3, 4)
# (1, 2, 3)
# (1, 2, 4)
# (1, 3, 4)
# (2, 3, 4)

for subset in itertools.chain.from_iterable(itertools.combinations(a, n) for n in range(len(a) + 1)):
    print(subset)

# ()
# (1,)
# (2,)
# (3,)
# (4,)
# (1, 2)
# (1, 3)
# (1, 4)
# (2, 3)
# (2, 4)
# (3, 4)
# (1, 2, 3)
# (1, 2, 4)
# (1, 3, 4)
# (2, 3, 4)
# (1, 2, 3, 4)
