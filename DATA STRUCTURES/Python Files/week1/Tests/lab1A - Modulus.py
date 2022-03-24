#================================
#   program:           Lab 1 A
#   name:              Kamil Szwed
#   date:              Jan 18 22
#   obj:               Modulus
#================================


#mainProgram


eggs = int(input("How many eggs do you want "))
dozens = eggs // 12
indiv = eggs % 12
# or indiv = eggs - dozens*12
price = dozens * 3.25 + indiv * 0.45
print("Price is ", price," dollars")





