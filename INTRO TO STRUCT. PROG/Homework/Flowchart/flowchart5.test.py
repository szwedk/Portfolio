#=======================================
#   File:       flowchart5.test
#   Date:       October 22, 2021
#   Name:       Kamil Szwed
#=======================================

#Start Program

id = int(input("Input an ID Number ==> "))
while not(id == -999):
    t1 = int(input("Input test #1 ==> "))
    t2 = int(input("Input test #2 ==> "))
    t3 = int(input("Input test #3 ==> "))
    fe = int(input("Input final exam grade ==> "))
    ts = t1 +t2 +t3
    fs = fe * .4 + ts * .2
    print("Student ID is ", id, "The final score is", fs)
    id = int(input("Input an ID Number ==> "))
else:
    print("End of job")
#EndIF
             
             
             
