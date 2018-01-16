A = {1, 2, 3, 3}
print(A)
# set([1, 2, 3])
B = {3, 4, 5, 6, 7}
print(B)
# set([3, 4, 5, 6, 7])
print(A | B)
# set([1, 2, 3, 4, 5, 6, 7])
print(A & B)
# set([3])
print(A - B)
# set([1, 2])
print(B - A)
# set([4, 5, 6, 7])
print(A ^ B)
# set([1, 2, 4, 5, 6, 7])
print((A ^ B) == ((A - B) | (B - A)))
# True
