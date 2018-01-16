import collections

Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(x=1.0, y=2.0)
print(p)
# Point(x=1.0, y=2.0)
print(p.x)
# 1.0
print(p.y)
# 2.0
