a, b, c = 1, 2, 3
print(a) # 1
print(b) # 2
print(c) # 3

a, b, c = [1, 2, 3]
print(a, b, c) # (1, 2, 3)

a, (b, c), d = [1, (2, 3), 4]
print(a) # 1
print(b) # 2
print(c) # 3
print(d) # 4
