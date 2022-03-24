from KamilSzwed_Midterm2_FUNCTIONS import LinkedList

myList = LinkedList()

choice = 0
while choice !=7:
    print('')
    print('What would you like me to do?')
    print('')
    print(' 1: Add new pilot / Flt Hours / Salary')
    print(' 2: Print Pilot Name / Flt Hours / Salary')
    print(' 3: Display name and salary of pilot with least flight hours')
    print(' 4: Print names of pilots with over 500 Flt Hours')
    print(' 5: Give pilots with a salary less than $50,000 a 10% raise')
    print(' 6: Display total amount of salaries paid')
    print(' 7: Exit')
    print('')
    choice = int(input('Enter Choice ==> '))
    print('')

    if choice == 1:
        name = input('Pilots Name: ')
        hours = float(input('Pilots Hours: '))
        salary = float(input('Pilots Salary: '))
        myList.insert(name,salary,hours)
    elif choice ==2:
        myList.p_list()
    elif choice ==3: 
        myList.least_hours()
    elif choice==4:
        myList.over_five()
    elif choice==5:
        myList.give_raise()
    elif choice==6:
        myList.total_paid()

print('Goodbye')
