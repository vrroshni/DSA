#from queue use lifoqueue
#for push lifoqueue has method->>put()
#for pop lifoqueue has method->>get()
#in this functions we have parameters such as timeout

import queue
stack=queue.LifoQueue(4)#4 is limit
stack.put(10)
stack.put(1)
stack.put(90)
stack.put(90)
# stack.put(890,timeout=1)#1 second

print(stack)

stack.get()
stack.get()
stack.get()
stack.get()
stack.get(timeout=1)#1 second