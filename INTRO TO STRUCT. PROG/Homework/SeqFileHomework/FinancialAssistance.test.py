#============================================
#   File:		book.py
#   Date:		Oct. 22, 2021
#   Purpose:	Sequential File Processing
#   Author:		Kamil Szwed
#============================================

#Start Program

ctf = 0
cpt = 0
sum = 0

info = open("vet.txt", mode = 'r')
student = []

print("                         Veterans")
print("                     Financial Assistance")
print("======================================")

for student in info:
    student = student.split()
    fn = student[0]
    code = int(student[1])
    units = int(student[2])
    deps = int(student[3])
    if code == 2:
        if  units <15 and deps <2:
            fs = 20 * units
        else:
            if units <15 and deps >=2:
                 fs = 23 * units
            #end if
        #end if
        if  units >=15 and deps <2:
            fs = 27 * units
        else:
            if units >=15 and deps >=2:
                 fs = 30 * units
            #end if
        #end if
        if units >=15:
            units = "FULL-TIME"
            ctf = ctf +1
        else:
            units = "PART-TIME"
            cpt = cpt + 1
        #end if
        sum = sum + fs
        print(fn," ",units," ",deps," ",fs)
    #end if
#end for
print("======================================")
print("Total full time students is: ", ctf)
print("Total part time students is: ", cpt)
print("Total financial aid is: $", sum)

print("EOJ")
#end program
            
        
    
    

