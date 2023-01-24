#implementing stack using modules
#use collections module and its class deque
#Deque have append and pop function


import collections
stack=collections.deque()
print(stack)


stack.append(12)
stack.append(1)
stack.append(34)
stack.append(15)
print(stack)


stack.pop()
print(stack)


print(len(stack)) #same as ordinary list
print(stack[-1])
print(not stack)