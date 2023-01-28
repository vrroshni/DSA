# lowest value,highest priority
# highest value,highest priority
# take priority in tuple
#using list


nw_list = []
nw_list.append(12)
nw_list.sort()
nw_list.append(14)
nw_list.sort()

nw_list.append(52)
nw_list.sort()

nw_list.append(72)
nw_list.sort()

nw_list.append(292)
nw_list.sort()

nw_list.pop()
print(nw_list)


import queue
q = queue.PriorityQueue()#default lower value
q.put(34)
q.put(67)
q.put(89)
q.put(604)
q.put(84)


print(q.get())

#to specify the priority in tuple

list1=[]
list1.append((1,"helloded"))
list1.append((5,"helldeo"))
list1.append((7,"hellofdd"))
list1.append((9,"hellweo"))

list1.sort()

print(list1)