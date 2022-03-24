#======================
#   Kamil Szwed
#   Feb 15, 22
#   LinkedLists 
#======================

class Node:
    def __init__(self, data):
        self.item = data 
        self.ref = None

class LinkedList:
    def __init__(self):
        self.start_node = None

def insert_at_start(self, data):
    new_node = Node(data) # Create the new node
    new_node.ref = self.start_node  # update the pointers
    self.start_node = new_node # start node is the new onde

#searching for something within the Llist
print('Searching a Llist')
def search_item(self,x):
    if self.start_node is None: 
        print(" List has no items") 
        return
    n = self.start_node 
    while n is not None:
        if n.item == x: 
            print("Item found") 
            return True
        n = n.ref
    print("Item not found")
    return False


#counting a node
print("This is counting a node within a Llist")
def get_count(self):
    if self.start_node is None:
        return 0
    n = self.start_node 
    count = 0
    while n is not None:
        count = count+1
        n = n.ref 
    return count

#printing a Llist
print("this is how to print a linked list")
def traverse_list(self):
    print("linked list: ", end = "")
    if self.start_node is None:
        print('List is empty')
        return
    else:
        return

#finihs this


#insterting a new first elelment
print('Inserting a new first elelment into a linked list')
def insert_at_start(self, data):
    new_node = Node(data) #creates a new node
    new_node.ref = self.start_node #updates the pointer
    self.start_node = new_node #start node is the new node

#instering a new node as the last element
print('Insert a new node at the end')
def inster_at_end(self,data):
    new_node = Node(data)
    if self.start_node is None:
        self.start_node = new_node
        return
    n = self.start_node
    while n.ref is not None:
        n = n.ref
    n.ref = new_node


#inserting after a certain item
print('Inster after a certain item')
def insert_after_item(self, x ,data):
    n = self.start_node
    print(n.ref)
    while n is not True:
        if n.item == x:
            break
        n = n.ref
    if n is None:
        print('Item not in list')
    else:
        new_node = Node(data)
        new_node.ref = n.ref
        n.ref = new_node

#deleting First node
print('Deleting the first node')
def delete_at_start(self):
    if self.start_node is None:
        print('Linked list is empty')
        return
    self.start_node = self.start_node.ref


#sorting a linked list
print('THis is how you sort a linked list')
def sort_list(self):
    return
    
    


 