#============================================
#	File:	Flowchart10.test
#	Name	K. Szwed
#	Date:	Oct. 23, 2021
#============================================

#Start Program

N = int(input("Input a number ==> "))

if not(N == -999):
	max = N
	min = N
	N = int(input("Input a number ==> "))
	while (N != -999):
		if N > max:
			max = N
		else:
			if N < min:
				min = N
			#end If
		#end if
		N = int(input("Input a number for N ==> "))
	#end while
else:
	print("Null List, max, min")
#end if
print("Your Max is:", max,"Your Min is:", min)
print("End of Job")
		
