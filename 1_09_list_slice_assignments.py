a = [1, 2, 3, 4, 5]
a[2:3] = [0, 0]
print(a) # insert [0, 0] into list between index 2 and 3
# [1, 2, 0, 0, 4, 5]
a[1:1] = [8, 9]
print(a)
# [1, 8, 9, 2, 0, 0, 4, 5]
a[1:-1] = []
print(a)
# [1, 5]
