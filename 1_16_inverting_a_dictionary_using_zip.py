m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(m.items())
# [('a', 1), ('c', 3), ('b', 2), ('d', 4)]
print(zip(m.values(), m.keys()))
# [(1, 'a'), (3, 'c'), (2, 'b'), (4, 'd')]
mi = dict(zip(m.values(), m.keys()))
print(mi)
# {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
