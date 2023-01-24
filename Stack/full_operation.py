stack = []

def push():
    number=int(input('Enter element :'))
    stack.append(number)
    print(stack)
  
  
def pop():
    if not stack:
      print('stack is empty!')
    else:
      e=stack.pop()
      print(e,"is removed")
      print(stack)




while True:
    print("Enter your choice \n 1.Push \n 2.Pop \n 3.Quit")
    choice = int(input('enter a num'))
    print('your choice is',choice)
    if choice == 1:
        push()
    elif choice== 2:
        pop()
    elif choice == 3:
        break
    else:
        print('Invalid Choice')