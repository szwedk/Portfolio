#+==========================
#   File:           TestGrades.Test
#   Name:        Kamil Szwed
#   Purp:           To read a sequential file
#+==========================

c = 0
sumGrades = 0
infile = open("grades.txt",'r')
for stud in infile:
    stud = stud.split()
    c = c + 1
    id = int(stud[0])
    fn = stud[1]
    ln = stud[2]
    t1 = int(stud[3])
    t2 = int(stud[4])
    t3 = int(stud[5])
    fe = int(stud[6])
    fs = 0.2 * (t1 + t2 + t3) + 0.4 * fe
    sumGrades = sumGrades +fs
    print(id, fn, ln ,fs)
#end for stud
infile.close()
avgGrade = sumGrades /  c

print("Number of students found in this file is: ", c)
print("Average grdae of all students is ", avgGrade)
#end Main
