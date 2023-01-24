stack=[]
#operations are happening at the same end (FILO,LIFO)
#add elemnt at the end of the list
stack.append(12)
stack.append(23)
stack.append(36)
print(stack)



#instead of all those append
stack.extend(3,4,5,6,8)

#remove the elment from the end
stack.pop()
print(stack)


#to check whether stack is empty
print(len(stack))
print(len(stack)==0)# same usage
print(not stack)# same usage


#accessing element at the top
stack.append(1)
stack.append(3)
stack.append(6)
print(stack[-1])



