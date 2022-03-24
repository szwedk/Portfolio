#============================================
#   File:		book.py
#   Date:		Oct. 22, 2021
#   Purpose:	Sequential File Processing
#   Author:		Kamil Szwed
#============================================

#Start Program

#initialize counter and accumulator
c = 0
sum = 0.0

#open bookFile.txt
info = open("bookFile.txt", mode='r')
writer = []

for writer in info:
        writer = writer.split()
        fn = writer[0]
        ln = writer[1]
        t1 = int(writer[2])
        t2 = int(writer[3])
        t3 = int(writer[4])
        fe = int(writer[5])
        fs = (t1 + t2 + t3)*0.2 + fe*0.4
        print(fn, " ",ln," ",fs)
        sum = sum + fs	#accum
        c = c + 1	#update counter

#end for writer
info.close()	#close file bookFile.txt
        
aveGrade = sum / c

print("\nTotal students processed is ",c)
print("The average grade for the class is", aveGrade)


