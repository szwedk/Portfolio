from MCP_FCTNS import morse_Code_Palindrome

my_list = morse_Code_Palindrome()

choice = 0
while choice != 4:
    print(" 1 = Press 1 to insert a Palindrome ")
    print(" 2 = Print mathematical EQ")
    print(" 3 = calculate if Palindrome is valid")
    print(" 4 = End")
    choice = int(input('Enter a choice ==> '))

    if choice ==1:
        Eq = input(" Enter an Palindrome => ")
    elif choice ==2:
        print(Eq)
    elif choice ==3:
        for x in Eq:
            if x == "A":
                my_list.push(x)
            elif x =='B':
                my_list.push(x)
            elif x =='C':
                my_list.push(x)
            elif x =='D':
                my_list.push(x)
            elif x =='E':
                my_list.push(x)
            elif x =='F':
                my_list.push(x)
            elif x =='G':
                my_list.push(x)
            elif x =='H':
                my_list.push(x)
            elif x =='I':
                my_list.push(x)
            elif x =='J':
                my_list.push(x)
            elif x =='K':
                my_list.push(x)
            elif x =='L':
                my_list.push(x)
            elif x =='M':
                my_list.push(x)
            elif x =='N':
                my_list.push(x)
            elif x =='O':
                my_list.push(x)
            elif x =='P':
                my_list.push(x)
            elif x =='Q':
                my_list.push(x)
            elif x =='R':
                my_list.push(x)
            elif x =='S':
                my_list.push(x)
            elif x =='T':
                my_list.push(x)
            elif x =='U':
                my_list.push(x)
            elif x =='V':
                my_list.push(x)
            elif x =='W':
                my_list.push(x)
            elif x =='X':
                my_list.push(x)
            elif x =='Y':
                my_list.push(x)
            elif x =='Z':
                my_list.push(x)

            elif x == "Z":
                y = my_list.pop()
                if y != 'Z':
                    print('I found a bug')
                    break
            elif x =='Y':
                y = my_list.pop(x)
                if y != 'Y':
                    print('I found a bug')
                    break
            elif x =='X':
                y = my_list.pop(x)
                if y !=  'X':
                    print('I found a bug')
                    break
            elif x == "W":
                y = my_list.pop()
                if y != 'W':
                    print('I found a bug')
                    break
            elif x =='V':
                y = my_list.pop(x)
                if y != 'V':
                    print('I found a bug')
                    break
            elif x =='U':
                y = my_list.pop(x)
                if y !=  'U':
                    print('I found a bug')
                    break
            elif x == "T":
                y = my_list.pop()
                if y != 'T':
                    print('I found a bug')
                    break
            elif x =='S':
                y = my_list.pop(x)
                if y != 'S':
                    print('I found a bug')
                    break
            elif x =='R':
                y = my_list.pop(x)
                if y !=  'R':
                    print('I found a bug')
                    break
            elif x == "Q":
                y = my_list.pop()
                if y != 'Q':
                    print('I found a bug')
                    break
            elif x =='P':
                y = my_list.pop(x)
                if y != 'P':
                    print('I found a bug')
                    break
            elif x =='O':
                y = my_list.pop(x)
                if y !=  'O':
                    print('I found a bug')
                    break
            elif x == "N":
                y = my_list.pop()
                if y != 'N':
                    print('I found a bug')
                    break
            elif x =='M':
                y = my_list.pop(x)
                if y != 'M':
                    print('I found a bug')
                    break
            elif x =='L':
                y = my_list.pop(x)
                if y !=  'L':
                    print('I found a bug')
                    break
            elif x == "K":
                y = my_list.pop()
                if y != 'K':
                    print('I found a bug')
                    break
            elif x =='J':
                y = my_list.pop(x)
                if y != 'J':
                    print('I found a bug')
                    break
            elif x =='I':
                y = my_list.pop(x)
                if y !=  'I':
                    print('I found a bug')
                    break
            elif x == "H":
                y = my_list.pop()
                if y != 'H':
                    print('I found a bug')
                    break
            elif x =='G':
                y = my_list.pop(x)
                if y != 'G':
                    print('I found a bug')
                    break
            elif x =='F':
                y = my_list.pop(x)
                if y !=  'F':
                    print('I found a bug')
                    break
            elif x =='E':
                y = my_list.pop(x)
                if y != 'E':
                    print('I found a bug')
                    break
            elif x =='D':
                y = my_list.pop(x)
                if y !=  'D':
                    print('I found a bug')
                    break
            elif x =='C':
                y = my_list.pop(x)
                if y != 'C':
                    print('I found a bug')
                    break
            elif x =='B':
                y = my_list.pop(x)
                if y !=  'B':
                    print('I found a bug')
                    break
            elif x =='A':
                y = my_list.pop(x)
                if y != 'A':
                    print('I found a bug')
                    break

        if my_list.get_count() != 0:
            print(' Not Valid')
        else:
            print('Valid')
print('goodbye')  