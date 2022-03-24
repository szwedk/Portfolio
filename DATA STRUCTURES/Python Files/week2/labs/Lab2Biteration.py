#====================
#   File:       Lab2B part 2
#   Name:       Kamil Szwed
#   Date:       Jan 25, 2022
#   Purpose:     
#=====================

#ftn
import math

def getArea(r):
    area = math.pi * r*r
    return area

def getCircum(r):
    circumference = 2 * math.pi * r
    return circumference

#mainProgram


print('======================================')
print('Radius     Area        Circumference')
print('======================================')

for r in range(1,11):
    print(r,'\t', round(getArea(r),3),'\t', round(getCircum(r),3))

print('======================================')
