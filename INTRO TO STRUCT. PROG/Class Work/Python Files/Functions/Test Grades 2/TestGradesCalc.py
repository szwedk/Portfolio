#================================================
#   File:           TestGradesCalc
#   Name:       Kamil Szwed
#   Date:         November 17, 2021
#   Purpose:    Modulize main Program using functions and reading from a data file
#================================================

def headers():
    print("\n            Student Grades")
    print("\n            ID         First       Last          Grade")
    print("\n            ==============================")
#end Ftn Headers

def outTotals(no, totalG):#the changed name
    print("Total students found in file is: ", no)
    print("Total grades is: ",totalG)
#end ftn outTotals

def calcGrades (students):
    c = 0
    tGrades = 0.0#can copy names in ftn that is the same in main prgram although have different meaning
    for stud in students:
        id = stud[0]
        fn = stud[1]
        ln = stud[2]
        t1 = int(stud[3])
        t2 = int(stud[4])
        t3 = int(stud[5])
        fe = int(stud[6])
        fs = .2 * (t1 +t2 +t3) + 0.4 * fe
        print(id, fn, ln, fs)
        c = c + 1
        tGrades = tGrades +fs
        #end for student
    return no, tGrades#gets renamed to c and tGrades in main program
#end ftn calcGrades

def getData():
    info = open('grades.txt','r')
    for student in info:
        print(student, student[0],student[1],student[4])
    #end for loop
    info.close()


#main Program
headers()
students = getData()
#c, tGrades = calcGrades (students)
#outTotals (c, tGrades) #change name in different enviorment


#end Main
