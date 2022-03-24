#challenge

# create a code that traverses a 
# linked list and figures out if 
# all parethesis are compatable





class Node:
    def __init__(self, data):
        self.item = data
        self.next = None

class stack_class:
    #create empty linked list
    def __init__(self):
        self.start_node = None

    def push(self, data):
        #adds new item to the top of stack
        new_node = Node(data)
        new_node.next = self.start_node
        self.start_node = new_node

    def pop(self):
        #removes most previous item added to top of stack
        if self.start_node is None:
            print('Stack is empty')
            return
        x = self.start_node.item
        self.start_node = self.start_node.next
        return x

    def get_count(self):
        #self counter allows for program to check if stack is empty
          if self.start_node is None:
               return 0
          n = self.start_node
          count = 0
          while n is not None:
               count = count+1
               n = n.next
          return count
#







