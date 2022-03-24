def output(x):
    print("The answer is ",x)
    return 'The end'
#end ftn output
    
def process(x,y,z):
    sum = x + y + z
    return sum
#end ftn process

def getData():
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = int(input("Enter c:"))
    return a,b,c
#end ftn getData
    
# main
a,b,c = getData()
ans = process(a,b,c)
msg = output(ans)
print(msg)

#end main
