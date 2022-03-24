from StacksCftns import stack_class

my_list = stack_class()

choice = 0
while choice != 4:
    print(" 1 = Press 1 to insert a Mathematical EQ ")
    print(" 2 = Print mathematical EQ")
    print(" 3 = calculate if parethesis are valid")
    print(" 4 = End")
    choice = int(input('Enter a choice ==> '))

    if choice ==1:
        Eq = input(" Enter an Equasion with brackets => ")
    elif choice ==2:
        print(Eq)
    elif choice ==3:
        for x in Eq:
            if x == "(":
                my_list.push(x)
            elif x =='[':
                my_list.push(x)
            elif x =='{':
                my_list.push(x)
            elif x == "}":
                y = my_list.pop()
                if y != '{':
                    print('I found a bug')
                    break
            elif x =='[':
                y = my_list.pop(x)
                if y != ']':
                    print('I found a bug')
                    break
            elif x =='(':
                y = my_list.pop(x)
                if y !=  ')':
                    print('I found a bug')
                    break
        if my_list.get_count() != 0:
            print(' Not Valid')
        else:
            print('Valid')
print('goodbye')  