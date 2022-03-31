class Node:
   def __init__(self, data):
         self.item = data
         self.left = None
         self.right = None
         
   def insert(self, data):
        ''' For inserting the data in the Tree '''
        if self.item == data:
            return False        # As BST cannot contain duplicate data

        elif data < self.item:
            ''' Data less than the root data is placed to the left of the root '''
            if self.left :
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True

        else:
            ''' Data greater than the root data is placed to the right of the root '''
            if self.right :
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True
               
   def minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while(current.left  is not None):
            current = current.left 

        return current

   def delete(self, data):
        ''' For deleting the node '''
        if self is None:
            return None

        # if current node's data is less than that of root node, then only search in left subtree else right subtree
        if data < self.item and self.left:
            print("going left")
            self.left  = self.left.delete(data)
        elif data > self.item and self.right:
            print("going right") 
            self.right = self.right.delete(data)
        elif data == self.item  :
            # deleting node with zero or one child
            if self.right is not None and self.left is None:
                print("right child only")
                temp = self.right
                self.item = self.right.item
                self.right = self.right.delete(temp.item)
                return temp
            elif self.left is not None and self.right is None:
                print("left child only") 
                temp = self.left
                self.item = self.left.item
                self.left = self.left.delete(temp.item)
                return temp
            elif self.left is  None and self.right is None:
                 print("zero children")
                 self= None
                 return None

            # deleting node with two children
            # first get the inorder successor
            print("Two children")
            temp = self.minValueNode(self.right)
            self.item = temp.item
            self.right = self.right.delete(temp.item)

        return self

   def find(self, data):
        ''' This function checks whether the specified data is in tree or not '''
        if(data == self.item):
            return True
        elif(data < self.item):
            if self.left:
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False

   def preorder(self):
        '''For preorder traversal of the BST '''
        if self:
            print( self.item, end = ' ')
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

   def inorder(self):
        ''' For Inorder traversal of the BST '''
        if self:
            if self.left:
                self.left.inorder()
            print(self.item, end = ' ')
            if self.right:
                self.right.inorder()

   def postorder(self):
        ''' For postorder traversal of the BST '''
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(self.item, end = ' ')
        
   def count(self):
       if self:
         c = 1   
         if self.left:
              c = c + self.left.count()
         if self.right:
              c = c + self.right.count()     
         return c
       else:
         return 0

   def getsum(self):
       if self:
         sum = self.item 
         if self.left:
              sum = sum + self.left.getsum()
         if self.right:
              sum = sum + self.right.getsum()  
         return sum
       else:
         return 0

   def height(self):
       if self:
           if self.left:
               l = self.left.height()
           else:
               l = -1
           if self.right:
               r = self.right.height()
           else:
               r = -1
           if l > r:
               h = 1 + l
           else:
                h = 1 + r
           return h
       else:
         return 0       
                
class BinaryTree:
     # ---------------Create an empty tree -------------
     
   def __init__(self):
         self.root = None
           
    #  ------------- Insert data  ----------------------
  
                   
   def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
 #  ------------ Delete nodes ---------------------------                         
   def delete(self, data):
        if self.root  :
            return self.root.delete(data)
 #  ------------ Search ---------------------------    
   def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False
 #  ------------ PreOrder ---------------------------  
   def preorder(self):
        if self.root is not None:
            print()
            print('Preorder: ')
            self.root.preorder()
 #  ------------ InOrder ---------------------------  
   def inorder(self):
        print()
        if self.root is not None:
            print('Inorder: ')
            self.root.inorder()
 #  ------------ PostOrder ---------------------------  
   def postorder(self):
        print()
        if self.root is not None:
            print('Postorder: ')
            self.root.postorder()
 #  ------------ Count nodes ---------------------------  
   def get_count(self):
        print()
        if self.root:
            c = self.root.count()
        else:
            c = 0 
        print('Count is ', c);  
 #  ------------ Sum nodes ---------------------------  
   def get_sum(self):
        print()
        if self.root:
            c = self.root.getsum()
        else:
            c = 0 
        print('Sum is ', c);  
 #  ------------ Height nodes ---------------------------  
   def get_height(self):
        print()
        if self.root:
            h = self.root.height()
        else:
            h = 0 
        print('Height is ', h);  
