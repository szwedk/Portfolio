# Kamil Szwed
# Practice
# 

class Node:
    def __init__(self,nm,rd):
        self.empName = nm
        self.empRec = rd
        self.next = None

class LinkedList:

    def __init__(self):
        self.start_node = None

    def printL(self):
        print('empName     Best empRec')
        print('---------------')
        if self.start_node is None:
            print('List is empty')
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.empName, n.empRec, sep = '\t')
                n = n.next
            print(' ')

    def ins(self,n,r):
        new_node = Node(n,r)
        new_node.next = self.start_node
        self.start_node = new_node

    def abov35(self):
        print('Players with empRec > 35: ', end = '\n')
        if self.start_node is None:
            print('List is empty')
            return
        else:
            n = self.start_node
            while n is not None:
                if n.empRec > 35:
                    print(n.empName,n.empRec, sep = '\t')
                n = n.next
        print(' ')

    def hiEmpRec(self):
        print('Highest empRec: ', end = '\n')
        if self.start_node is None:
            print('List is empty')
            return
        else:
            max_empRec = 0
            n = self.start_node
            while n != None:
                if max_empRec < n.empRec:
                    max_empRec = n.empRec
                    max_empName = n.empName
                n = n.next
            print(max_empName, max_empRec, sep = '\t')

# Kamil Szwed
# Practice
# 

My_List = LinkedList()

choice = 0
while choice != 5:
    print(' ')
    print('What do you want to do?')
    print('1 = Add a new player')
    print('2 = Print all players')
    print('3 = Print players with empRec above 35')
    print('4 = Print player with highest empRec')
    print('5 = Exit')
    print(' ')
    choice = int(input('Enter Choice: '))
    print(' ')

    if choice == 1:
        empName = input('Enter empName: ')
        empRec = float(input('Enter empRec: '))
        My_List.ins(empName,empRec)
    elif choice == 2:
        My_List.printL()
    elif choice == 3:
        My_List.abov35()
    elif choice == 4:
        m = My_List.hiEmpRec()
        

print('\n Goodbye \n')
    
