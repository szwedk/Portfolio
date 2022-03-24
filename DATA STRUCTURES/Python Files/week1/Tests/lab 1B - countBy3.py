#============================================
#   File:		countBy3
#   Name:       Kamil Szwed
#   Date:		Jan. 20, 22
#   Purpose:	Write a program that counts by threes
#                                    from 0 to 300 (0, 3, 6, 9, ... 300). The program should
#                                    start a new line at multiples of 30 (30 numbers per line).
#============================================

#mainProgram

i = 0
for i in range (0,303,3):
    print(i, end=', ')
    if i % 90 == 0:
        print(' ')

#endProgram



