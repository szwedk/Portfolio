class Node:
    def __init__(self,nm,rd):
        self.name = nm
        self.record = rd
        self.ref = None

class LinkedList:

    def __init__(self):
        self.start_node = None

    def print_list(self):
        print('Name     Best Record')
        print('---------------')
        if self.start_node is None:
            print('List is empty')
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.name, n.record, sep = '\t')
                n = n.ref
            print(' ')

    def insert(self,n,r):
        new_node = Node(n,r)
        new_node.ref = self.start_node
        self.start_node = new_node

    def record_above_35(self):
        print('Players with record > 35: ', end = '\n')
        if self.start_node is None:
            print('List is empty')
            return
        else:
            n = self.start_node
            while n is not None:
                if n.record > 35:
                    print(n.name,n.record, sep = '\t')
                n = n.ref
        print(' ')

    def highest_record(self):
        print('Highest Record: ', end = '\n')
        if self.start_node is None:
            print('List is empty')
            return
        else:
            max_record = 0
            n = self.start_node
            while n != None:
                if max_record < n.record:
                    max_record = n.record
                    max_name = n.name
                n = n.ref
            print(max_name, max_record, sep = '\t')



My_List = LinkedList()

choice = 0
while choice != 5:
    print(' ')
    print('What do you want to do?')
    print('1 = Add a new player')
    print('2 = Print all players')
    print('3 = Print players with record above 35')
    print('4 = Print player with highest record')
    print('5 = Exit')
    print(' ')
    choice = int(input('Enter Choice: '))
    print(' ')

    if choice == 1:
        name = input('Enter Name: ')
        record = float(input('Enter Record: '))
        My_List.insert(name,record)
    elif choice == 2:
        My_List.print_list()
    elif choice == 3:
        My_List.record_above_35()
    elif choice == 4:
        m = My_List.highest_record()
        

print('\n Goodbye \n')
    
