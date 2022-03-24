#=======================================
#   File:       flowchart9.test
#   Date:       October 22, 2021
#   Name:       Kamil Szwed
#=======================================

#Start Program

x = int(input("Input a value for 'x': "))
y = int(input("Input a value for 'y': "))

while not(x + y > 42):
    x = x + 10
    y = y + 3
    print(x,y)
#endwhile
print("42")

#eng program
