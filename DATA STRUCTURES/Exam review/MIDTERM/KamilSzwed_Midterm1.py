#==================================================================
#   File:           KamilSzwed_Midterm1
#   Name:           Kamil Szwed
#   Prof:           Professor Senbal
#   Date:           March 1, 2022
#   Purpose:        Tuesday Midterm
#==================================================================

import math
import numpy as np

#Main

salary = []
names = []
hours = []


choice = 0 
while choice != 7:
    print(' ')
    print('What would you like me to do?')
    print('1 = Add Pilot Name, Salary, Hours')
    print('2 = Print Name, Salary, Flt Hours of all current Pilots: ')
    print('3 = Display Name and salary of Pilot with least hours: ')  #len(names)
    print('4 = Print Names of Pilots with more than 500 Flt Hours: ')
    print('5 = Give Pilots with salary less than $50,000 a 10% raise')
    print('6 = Total amount of salaries paid: ') #run for loop for total
    print('7 = exit')
    print('\t')
    choice = int(input('Enter a choice:  '))
    print('\t')

    if choice ==1:
        name = input('Pilot Name: ')
        slry = float(input('Pilot Salary: '))
        Flthours = float(input('Pilots Flight Hours: '))
        names.append(name)
        salary.append(slry)
        hours.append(Flthours)

    elif choice ==2:
        if len(names) == 0:
            print('List is empty')
        else:
            print('Names\t\tFLT Hours\tSalary')
            print('-----------------------------------------')
            for i in range(len(names)):
                print(names[i], format(hours[i]), format(salary[i]), sep='\t\t')
    
    elif choice ==3:  
        if len(names) ==0:
            print('List is empty')
        else:
            min = hours[0]
            for i in range (len(hours)):
                if hours[i] < min:
                    min = hours[i]
            print (f'Pilot {name} with a salary of ${salary[i]} has the least flight hours: {min}')

    elif choice ==4:
        if len(names) ==0:
            print('List is empty')
        else:
            print('Pilots with more than 500 flight hours')
            print('-----------------------------------------')
            for i in range(len(hours)):
                if hours[i] > 500:
                    print(names[i],' has ', format(hours[i]), ' Flight Hours')

    elif choice ==5:
        if len(names)==0:
            print('List is empty')
        else:
            print('Pilot Salaries under 50k recieved a 10% raise')
            print('----------------------------------------------')
            x = 0
            for i in range(len(salary)):
                if salary[i] < 50000:
                    x = salary[i] * .1
                    salary[i] = salary[i] + x
                    print(f'{names[i]} recieved a ${round(x, 2)} increase in pay, \nHis/Her new salary is ${round(salary[i], 2)}', end = '\n')


    elif choice ==6:
        if len(names)==0:
            print('List is empty')
        else:
            totSalary = 0
            for i in range(len(salary)):
                totSalary = totSalary + salary[i]
            print(f'Total salaries paid is ${round(totSalary, 2)}')

print('GoodBye')