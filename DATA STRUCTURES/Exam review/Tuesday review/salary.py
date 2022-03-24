#kamil szwed
#salary question

salary = []
names = []


choice = 0 
while choice != 7:
    print(' ')
    print('What do you want to do?')
    print('1 = Add Employee')
    print('2 = Print name and salary of all current employees')
    print('3 = Display number of employees')  #len(names)
    print('4 = Employees w/ salary greater than $100,000')
    print('5 = Give employee with salary less than $50,000 a 10% raise')
    print('6 = Total amount of salaries paid') #run for loop for total
    print('7 = exit')
    print('\t')
    choice = int(input('Enter a choice:  '))
    print('\t')



    if choice == 1:
        nE = input('Employee Name: ')
        nS = float(input('Employee Salary: '))
        names.append(nE)
        salary.append(nS)

    elif choice ==2:
        if len(names) == 0:
            print('List is empty')
        else:
            print('Names    Salary')
            print('----------------')
            for i in range(len(names)):
                print(names[i], format(salary[i]), sep = '\t')

    elif choice ==3:
        if len(names) ==0:
            print('List is Empty')
        else:
            print(f'Total Employees: {len(names)}')

    elif choice ==4:
        if len(names) ==0:
            print('List is empty')
        else:
            print('Salaries greater than $100,000')
            for i in range(len(salary)):
                if salary[i] > 100000:
                    print(names[i], format(salary[i]), sep = '\t')

    elif choice ==5:
        if len(names)==0:
            print('List is empty')
        else:
            print('These salaries under 50k recieved a 10% raise')
            x = 0
            for i in range(len(salary)):
                if salary[i] < 50000:
                    x = salary[i] * .1
                    salary[i] = salary[i] + x
                print(f'{names[i]} recieved a ${x} increase in pay, \nHis/Her new salary is {salary[i]}')

    elif choice ==6:
        if len(names)==0:
            print('List is empty')
        else:
            totSalary = 0
            for i in range(len(salary)):
                totSalary = totSalary + salary[i]
            print(f'Total salaries paid are {totSalary}')


print('Good Bye!')
