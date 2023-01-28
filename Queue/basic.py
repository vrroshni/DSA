#front-removal,rear-innsertion
queue=[]
queue.append(10)
queue.append(12)
queue.append(164)
queue.append(180)


print(queue)

queue.pop(0)
print(queue)
queue.pop(0)
print(queue)


#anotherway
#front-insertion,rear-removal

queue=[]
queue.insert(0,10)
queue.insert(0,50)
queue.insert(0,60)
queue.insert(0,90)
print(queue)

queue.pop()
print(queue)


queue=[]
print(not queue)#to check queue is empty
queue[-1]#for elememt at rear
queue[0]#for elememt at front