               
from QueueModule import Queue

My_Queue = Queue()

choice = 0
while choice != 5:
    print("\n Queue Demo, what do you want to do?")
    print(" 1 = Add to the end ")
    print(" 2 = Remove the first node ")
    print(" 3 = Print Queue")
    print(" 4 = Count number of elements inQueue ")
    print(" 5 = Exit ")
    choice = int(input("\n Enter Choice: "))

    if choice==1:
        num = int(input("\n Enter number to add: "))
        My_Queue.Add(num)
        print( num , " added to queue")
    elif choice==2:
        x = My_Queue.Remove()
        print(x,  " was removed ")
    elif choice==3:
        My_Queue.traverse_list()
    elif choice==4:
        x = My_Queue.get_count()
        print("Queue has ",x, " items now")
         
      
print("\n Goodbye \n")
