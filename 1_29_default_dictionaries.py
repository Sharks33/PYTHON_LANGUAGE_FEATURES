import collections

m = dict()
# print(m['a'])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'a'

m = collections.defaultdict(int)
print(m['a'])
# 0
print(m['b'])
# 0

m = collections.defaultdict(str)
print(m['a'])
# ''

m['b'] += 'a'
print(m['b'])
# 'a'

m = collections.defaultdict(lambda: '[default value]')
print(m['a'])
# '[default value]'

print(m['b'])
# '[default value]'
