

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


# Converts English to Morse Code
def eng_to_morse(message): 
    morse_code = '' 
    for letter in message:
            letter = letter.upper() 
            morse_code = morse_code + morse[letter] 
    return morse_code 

# Converts Morse to English
def morse_to_eng(message): 
    # Requires an extra space or misses last character
    message = message
    english = '' 
    letter = ''
    for morse_code in message: 
        # checks for space, when means a new character
        if (morse_code != ' '): 
            # storing morse code of a single character 
            letter = letter + morse_code 
        # in case of space 
        else: 
            english = english + list(morse.keys())[list(morse.values()).index(letter)] 
            letter = '' 
    return english 

test = eng_to_morse("test to test to test")
test2 = morse_to_eng("- . ... - / - --- / - . ... - / - --- / - . ... -")
print(test)
print(test2)