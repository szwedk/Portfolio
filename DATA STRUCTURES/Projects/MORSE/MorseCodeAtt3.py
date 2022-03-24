


#morse Library
morse = { 'A':'.-', 'B':'-...',
        'C':'-.-.', 'D':'-..', 'E':'.',
        'F':'..-.', 'G':'--.', 'H':'....',
        'I':'..', 'J':'.---', 'K':'-.-',
        'L':'.-..', 'M':'--', 'N':'-.',
        'O':'---', 'P':'.--.', 'Q':'--.-',
        'R':'.-.', 'S':'...', 'T':'-',
        'U':'..-', 'V':'...-', 'W':'.--',
        'X':'-..-', 'Y':'-.--', 'Z':'--..',
        '1':'.----', '2':'..---', '3':'...--',
        '4':'....-', '5':'.....', '6':'-....',
        '7':'--...', '8':'---..', '9':'----.',
        '0':'-----', }

#A class to implement a Node / Tree
class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

#Input a message for the computer to read  
def MsgInput():
    #Message Input
    message = (input("Enter a message ")).upper()
    morseCode = ""
    for i in range(len(message)):
        if i >= 80:
            message = str(input('Word too long \nInput String under 80 characters: '))
            message.upper()
        else:
            return message, morseCode

#Convert Character (Find the character using a pre-order travers of the Binary Tree
def getMorseCode(node, character, code):
  if node==None:
    return False
  elif node.value == character:
    return True
  else:  
    if getMorseCode(node.left, character, code)==True:
      code.insert(0,".")
      return True
    elif getMorseCode(node.right,character,code)==True:
      code.insert(0,"-")
      return True

#Convert the message, one character at a time    
def convertMessage(message, morseCode):   
    for character in message:
        dotsdashes = []
        getMorseCode(tree,character,dotsdashes)
        code = "".join(dotsdashes)
        morseCode = morseCode + code + " "
    return morseCode

#Figure out if message is symetrical
def OperationMessage(message):
    count = len(message)
    ValidorNot = 0
    if count % 2 == 0: #right now only works with even lettered words
        x=len(message)
        str1 = slice(0,len(message)//2)
        str2 = slice(len(message)//2,len(message))
        L = message[str1] 
        R = message[str2]
    return L, R

#check string is a palindrome or not
def isPalindrome(L,R):
    # reverse to string 
    rev = ''.join(reversed(L))
    Nrev = rev[1:]#removes extra space in front of string 
    print(Nrev)
    print(R)
    # Checking if both string are equal or not
    # Does not work
    flG = 0
    for i in range(len(Nrev)):
        if R[i]!= Nrev[i]:
            flG = 1
            print('inside loop',R[i],Nrev[i])
            break
    if flG ==0:
        print('They are the same')
    else:
        print('THey are different')



tree = Node("START") #The root node of  binary tree

# 1st Level
tree.left = Node("E")
tree.right = Node("T")

# 2nd Level
tree.left.left = Node("I")
tree.left.right = Node("A")
tree.right.left = Node("N")
tree.right.right = Node("M")

# 3rd Level
tree.left.left.left = Node("S")
tree.left.left.right = Node("U")
tree.left.right.left = Node("R")
tree.left.right.right = Node("W")

tree.right.left.left = Node("D")
tree.right.left.right = Node("K")
tree.right.right.left = Node("G")
tree.right.right.right = Node("O")

# 4th Level
tree.left.left.left.left = Node("H")
tree.left.left.left.right = Node("V")
tree.left.left.right.left = Node("F")
tree.left.left.right.right = Node("")
tree.left.right.left.left = Node("L")
tree.left.right.left.right = Node("")
tree.left.right.right.left = Node("P")
tree.left.right.right.right = Node("J")

tree.right.left.left.left = Node("B")
tree.right.left.left.right = Node("X")
tree.right.left.right.left = Node("C")
tree.right.left.right.right = Node("Y")
tree.right.right.left.left = Node("Z")
tree.right.right.left.right = Node("Q")
tree.right.right.right.left = Node("")
tree.right.right.right.right = Node("")



x, y = MsgInput()
morse = convertMessage(x, y)
#print(morse)
L, R = OperationMessage(x)
checkL = convertMessage(L,y)
checkR = convertMessage(R,y)

print(checkL,checkR)

ans = isPalindrome(checkL, checkR)




