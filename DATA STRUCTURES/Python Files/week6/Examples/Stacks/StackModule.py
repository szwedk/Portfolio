class Node:
     def __init__(self, data):
         self.item = data
         self.ref = None

class Stack:
     # ---------------Create an empty linked list -------------
     
     def __init__(self):
         self.top = None
         
     # --------------- Traverse the linked list  ----------------------
     
     def traverse_list(self):
         print("Stack: ", end = " ")
         if self.top is None:
             print("Stack is empty")
             return
         else:
             n = self.top
             while n is not None:
                 print(n.item, end =" " )
                 n = n.ref
         print(" ")        
                 
    #  ------------- PUSH  ----------------------
    
     def Push(self, data):
            new_node = Node(data)
            new_node.ref = self.top
            self.top = new_node
      
   #  ------------ Count nodes ---------------------------           

     def get_count(self):
          if self.top is None:
               return 0
          n = self.top
          count = 0
          while n is not None:
               count = count+1
               n = n.ref
          return count

     
   # -------------- Pop  ------------------

     def Pop(self):
            if self.top is None:
                print("Stack is empty!")
                return
            x = self.top.item  
            self.top = self.top.ref
            return x
 
