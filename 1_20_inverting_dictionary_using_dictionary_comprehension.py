m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(m)
# {'d': 4, 'a': 1, 'b': 2, 'c': 3}
print({v: k for k, v in m.items()})
# {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
