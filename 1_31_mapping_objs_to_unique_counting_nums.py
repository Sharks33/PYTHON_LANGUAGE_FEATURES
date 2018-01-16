import itertools, collections

value_to_numeric_map = collections.defaultdict(itertools.count().next)

print(value_to_numeric_map['a'])
# 0
print(value_to_numeric_map['b'])
# 1
print(value_to_numeric_map['c'])
# 2
print(value_to_numeric_map['a'])
# 0
print(value_to_numeric_map['b'])
# 1
