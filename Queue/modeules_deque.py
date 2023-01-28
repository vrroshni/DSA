import collections


#either append and pop || appendleft and pop

q=collections.deque()
# q.append(1)
# q.append(67)
# q.append(56)
# q.append(90)

# print(q)

# q.popleft()

# print(q)


q.appendleft(89)
q.appendleft(7)
q.appendleft(49)
q.appendleft(19)

print(q)


q.pop()
print(q)


print(q[-1])#last
print(q[0])#front