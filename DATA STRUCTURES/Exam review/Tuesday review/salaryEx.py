# Kamil Szwed
# Practice
# 
# code that adds employes and salary to a list
# prints the name and salary of current employees
# shows number of employees
# ppl that make more that 100k
# ppl that make less than 50k get 10% raise
# show total amount of salaries
#


ns= []
sy= []

choice = 0 
while choice !=7:
    print(' ')
    print('What do you want to do?')
    print('1 = Add Employee')
    print('2 = Print name and salary of all current employees')
    print('3 = Display number of employees')  #len(names)
    print('4 = Employees with a greater salary than $100,000')
    print('5 = Give employee with salary less than $50,000 a 10% raise')
    print('6 = Total amount of salaries paid') #run for loop for total
    print('7 = exit')
    print(' ')
    choice = int(input('Enter choice:  '))
    print(' ')

#    if choice !=7 and ns==0:
#        print('List is Empty')

    if choice ==1:
        nE = input('Employee Name: ')
        nS = float(input('Enter Salary: '))
        sy.append(nS)
        ns.append(nE)

    elif choice ==2:
        if len(ns) ==0:
            print('List is empty')
        else:
            print('Names\tSalary')
            print('-------------------')
            for i in range(len(ns)):
                print(ns[i], format(sy[i]), sep = "\t")

    elif choice==3:
        if len(ns)==0:
            print('List is empty')
        else:
            print(f'Total employees: {len(ns)}')

    elif choice ==4:
        if len(ns)==0:
            print('List is Empty')
        else:
            print('Employees whose salary is over 100,000')
            for i in range(len(sy)):
                if sy[i] > 100000:
                    print(ns[i], format(sy[i]), sep = '\t')

    elif choice==5:
        if len(ns)==0:
            print('List is Empty')
        else:
            x = 0
            for i in range(len(sy)):
                if sy[i] < 50000:
                    x = sy[i] * .1
                    sy[i] = sy[i] + x
                    print(f'{ns[i]} recieved a ${round(x,2)} raise, \nNew salary is {round(sy[i],2)}')

    elif choice==6:
        if len(ns)==0:
            print('List is Empty')
        else:
            totSalary = 0
            for i in range(len(sy)):
                totSalary = totSalary + sy[i]
            print(f'{len(ns)} employees paid a total of {round(totSalary,2)}')

print('Goodbye')




        
