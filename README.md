# Morse Code Translator in Python
This python class can both translate a string to morse code but also in reverse

# Morse Code Structure
- There is always (at least) a space after a peice of morse code to indicate a new character 
- To indicate a new word, the program will use a slash (/)
- If there are multible spaces between morse code bits in the method "translateToMorse", the program will just ignore them
 
# Program Structure

The Class is buit with 7 methods
- getMorse(no parameters)  
Method return the dictionary used in the class

- returnMorse(char)  
char is the string with the lengh of 1 that you want to convert to morse code

- returnChar(code)  
code the the morse code of one character (string with the lengh of 1) that you want to convert it to

- translateToMorse(sentence)  
sentence is the sentence you want to convert to morse code, the program will follow the "Morse Code Structure"

- translateToSentence(code)  
code is the morse code that you want to convert to a string

- doesCharExist(char)  
Checks if the given character exist in the dictionary, returns True if it exists

- doesMorseCodeExist(code)  
Checks if a given (morse) code exists in the dictionary
