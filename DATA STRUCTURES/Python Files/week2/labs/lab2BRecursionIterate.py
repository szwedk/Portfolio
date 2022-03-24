#====================
#   File:       Lab2B
#   Name:       Kamil Szwed
#   Date:       Jan 25, 2022
#   Purpose:     
#=====================

def FactRecursion( n):
   if (n==0):  # base case
     return 1
   else:
     return n * FactRecursion(n-1)

def FactIterate( n):
    fact = 1
    for i in range( 1, n+1):
        fact = fact * i
    return fact


n = -1
while n <0:
    n = int(input('Enter a positive integer: '))

fi = FactIterate(n)
print('Iterative answer is ', fi)
fr = FactRecursion(n)
print('Recursive answer is', fr)