




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


    
def characterNUM():
    EngWord = str(input('Enter a Palindrome: '))
    for i in len(EngWord):
        if i >= 80:
            EngWord = str(input('Word too long \nInput String under 80 characters: '))
    return EngWord

class Node:
   def __init__(self, data):
         self.item = data
         self.left = None
         self.right = None

   def insert(self, data):
        ''' For inserting the data in the Tree '''
        if self.item == data:
            return False        
        elif '-' == morse.keys  :
            ''' Data less than the root data is placed to the left of the root '''
            if self.left :
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            ''' Data greater than the root data is placed to the right of the root '''
            if self.right :
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True



