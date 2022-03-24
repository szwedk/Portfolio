class Node:
    def __init__(self, nm, sl, hr ):
        self.name = nm 
        self.salary = sl
        self.hours = hr
        self.next = None

class LinkedList:
     
    def __init__(self):
        self.start_node = None

    def insert(self,nm,sl,hr):
        new_node = Node(nm,sl,hr)
        new_node.next = self.start_node
        self.start_node = new_node

    def p_list(self):
        print('Name\tFlt Hours\tSalary')
        print('==================================')
        if self.start_node is None:
            print('List is empty')
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.name, n.hours, n.salary, sep = '\t')
                n = n.next
            print(' ')

    def least_hours(self): 
        print('Name\tFltHours')
        print('==================================')
        if self.start_node is None:
            print('List is empty')
            return
        else:
            min_name = str(' ')
            min_hours = 1000000
            n = self.start_node
            while n != None:
                if min_hours > n.hours:
                    min_hours = n.hours
                    min_name = n.name
                n = n.next
            print(min_name, min_hours, sep = '\t')
            print(' ')

    def over_five(self):
        print('Pilots over 500 Flt Hours\n')
        print('Name\tFlt Hours')
        print('==================================')
        if self.start_node is None:
            print('List is empty')
            return
        else:
            n = self.start_node
            while n is not None:
                if n.hours > 500:
                    print(n.name,n.hours, sep = '\t')
                n = n.next
        print(' ')

    def give_raise(self):
        print('Gave raise to these Pilots\n')
        print('==================================')
        if self.start_node is None:
            print('List is empty')
            return
        else:
            x = 0
            n = self.start_node
            while n is not None:
                if n.salary < 50000:
                    x = n.salary * .1
                    n.salary = n.salary + x
                    print(f'{n.name} recieved a ${round(x, 2)} increase in pay')
                    print(f'His/Her new salary is ${round(n.salary, 2)}', end = '\n')
                n = n.next

    def total_paid(self):
        if self.start_node is None:
            print('List is empty')
            return
        else:
            totSalary = 0
            n = self.start_node
            while n is not None:
                totSalary = totSalary + n.salary
                n = n.next
            print(f'Total salaries paid is ${round(totSalary, 2)}')
                










    