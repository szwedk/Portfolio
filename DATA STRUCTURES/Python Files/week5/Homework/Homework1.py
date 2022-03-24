#CS112 Data Structures
#Homework 5, Linked Lists

#A greengrocer would like to maintain a linked lists about his products. 
# For each product he saves it name, price and stock amount.
#Write a program that creates an empty linked list 
# and then prompts to user to do one of the following:

#1. Add a product to the list (anywhere)
#2. Print all products in the LinkedList
#3. Print all products above a certain price
#4. Print all low-stock products ( Less than 20 pounds)
#5. Exit

#Hint: The trick here is to make a node with 4 parts: 
# one for the produce name, one for the price, 
# one for the stock and one a ref to the next node.


import string
from traceback import print_exception
from unicodedata import name


class Node:
     def __init__(self, nm, pr, st):
         self.name = nm
         self.price = pr
         self.stock = st
         self.ref = None

class LinkedList:
     # ---------------Create an empty linked list -------------
     
    def __init__(self):
         self.start_node = None

    #  ------------- Insert at start  ----------------------
    
    def insert_at_start(self, nm, pr, st):
            new_node = Node(nm, pr, st)
            new_node.next = self.start_node
            self.start_node = new_node
            if self.start_node is None:
                print('\n List is empty')
                return
    
    def print_prod(self):
        if self.start_node is None:
            print('\n No products availabe ')
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.name, n.price, n.stock)
                n = n.next

    def print_above(self,x):
           if self.start_node is None:
               print("\n List has no items")
               return
           n = self.start_node
           res = []
           while n is not None:
               if n.price >= x:    
                    res.append(n.name)

               n = n.next
           print(f'\n The following products were found \n {res}')
           return True

    def print_low_stock(self):
           if self.start_node is None:
               print("\n List has no items")
               return
           n = self.start_node
           resa = []
           while n is not None:
               if n.stock <= 20:    
                    resa.append(n.name)

               n = n.next
           print(f'\n The following products are low in stock \n {resa}')
           return True


#main

My_List = LinkedList()

choice = 0
while choice != 5:
    print(" 1 = Insert name, price, stock ")
    print(" 2 = Print all products")
    print(" 3 = Search all products above inserted price")
    print(" 4 = Print all low-stock products ")
    print(" 5 = exit ")
    choice = int(input("\n Enter Choice: "))


    if choice==1:
        x = input('Name of Product => ')
        y =float(input('Price of Product => '))
        z =int(input('Stock of Product => '))
        My_List.insert_at_start(x,y,z)
        print(f'\n Item {x} added at ${y} with {z} in stock')
    elif choice==2:
        print(f'\n{My_List.print_prod()}')
    elif choice==3:
        num = float(input('\n Show product above this price => $'))
        My_List.print_above(num)
    elif choice==4:
        print(f'\n {My_List.print_low_stock()}')


print("\n Goodbye \n")
