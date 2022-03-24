               
from TreeModule import BinaryTree


My_Tree = BinaryTree()

choice = 0
while choice != 6:
    print("\n Binary Search Tree Demo, what do you want to do?")
    print(" 1 = Insert data ")
    print(" 2 = Traverse and print Tree inorder ")
    print(" 3 = Count number of nodes ")
    print(" 4 = Search for an item ")
    print(" 5 = Delete an item ")
    print(" 6 = Exit")
    
    choice = int(input("\n Enter Choice: "))

    if choice==1:
        num = int(input("\n Enter number to add to tree: "))
        My_Tree.insert( num)
        print( num , " inserted")
    elif choice==2:
        My_Tree.inorder()
    elif choice==3:
        My_Tree.get_count()
         
    elif choice ==4:
        x = int(input(" Enter number to search for: "))
        answer = My_Tree.find(x)
        if answer:
            print("Found it")
        else:
            print("Not found") 
    elif choice ==5:
        x = int(input(" Enter number to delete: "))
        answer = My_Tree.delete(x)
        if answer== None:
            My_Tree.root = None
         
          
    
      
print("\n Goodbye \n")
