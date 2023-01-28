queue=[]
def enqueue():
    if limit==len(queue):
        print('Queue is Full')
    else:
        print('Enter Number')
        num=int(input())
        queue.append(num)
        
def dequeue():
    if not queue:
        print('Queue is Empty')
    else:
        queue.pop(0)

def show():
    print(queue)

limit=int(input("Enter the limit"))
while True:
    choice=int(input("Enter the choice: \n1.Enque \n2.Dequeue \n3.Show"))
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        show()
    else:
        break