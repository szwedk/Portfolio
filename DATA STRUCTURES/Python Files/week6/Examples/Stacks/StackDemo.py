               
from StackModule import Stack

My_Stack = Stack()

choice = 0
while choice != 5:
    print("\n Stack Demo, what do you want to do?")
    print(" 1 = Push ")
    print(" 2 = Pop ")
    print(" 3 = Print Stack")
    print(" 4 = Count stack ")
    print(" 5 = Exit ")
    choice = int(input("\n Enter Choice: "))

    if choice==1:
        num = int(input("\n Enter number to push: "))
        My_Stack.Push(num)
        print( num , " pushed on stack")
    elif choice==2:
        x = My_Stack.Pop()
        print(x,  " was popped out")
    elif choice==3:
        My_Stack.traverse_list()
    elif choice==4:
        x = My_Stack.get_count()
        print("Stack has ",x, " items now")
         
      
print("\n Goodbye \n")
