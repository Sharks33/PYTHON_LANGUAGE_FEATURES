import collections

Q = collections.deque()
Q.append(1)
Q.appendleft(2)
Q.extend([3, 4])
Q.extendleft([5, 6])
print(Q)
# deque([6, 5, 2, 1, 3, 4])
print(Q.pop())
# 4
print(Q.popleft())
# 6
print(Q)
# deque([5, 2, 1, 3])
Q.rotate(3)
print(Q)
# deque([2, 1, 3, 5])
Q.rotate(-3)
print(Q)
# deque([5, 2, 1, 3])
