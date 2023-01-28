import queue
q=queue.Queue(maxsize=5)
# q.put_nowait(12)#block =false,it won't wait 
# q.put_nowait(11)
# q.put_nowait(126)
# q.put_nowait(189)

# e=q.get_nowait()
# print(e)


q.put(12)#block =true,it won't print meessages such as q is full or empty ,it will wait until its available
q.put(34)
q.put(56)
q.put(78)

e=q.get()
print(e)
q.empty()#empty or not
q.full()#full or not