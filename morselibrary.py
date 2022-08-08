class morseLibrary:
    __library = {
        "A" : ".-",
        "B" : "-...",
        "C" : "-.-.",
        "D" : "-..",
        "E" : ".",
        "F" : "..-.",
        "G" : "--.",
        "H" : "....",
        "I" : "..",
        "J" : ".---",
        "K" : "-.-",
        "L" : ".-..",
        "M" : "--",
        "N" : "-.",
        "O" : "---",
        "P" : ".--.",
        "Q" : "--.",
        "R" : ".-.",
        "S" : "...",
        "T" : "-",
        "U" : "..-",
        "V" : "...-",
        "W" : ".--",
        "X" : "-..-",
        "Y" : "-.--",
        "Z" : "--..",
        "1" : ".----",
        "2" : "..---",
        "3" : "...--",
        "4" : "....-",
        "5" : ".....",
        "6" : "-....",
        "7" : "--...",
        "8" : "---..",
        "9" : "----.",
        "0" : "-----",
        "." : ".-.-.-",
        "," : "--..--",
        "?" : "..--..",
        "'" : ".----.",
        "!" : "-.-.--",
        "/" : "-..-.",
        "(" : "-.--.",
        ")" : "-.--.-",
        "&" : ".-...",
        ":" : "---...",
        ";" : "-.-.-.",
        "=" : "-...-",
        "+" : ".-.-.",
        "-" : "-....-",
        "_" : "..--.-",
        '"' : ".-..-.",
        "$" : "...-..-",
        "@" : ".--.-."
    }

    # Returns the dictionary used in the class
    def getMorse(self):
        return self.__library

    # Returns True if the character exist
    def doesCharExist(self, char):
        if char[len(char) - 1] == " ":
            char = char[:len(char)-1]
        for i in morseLibrary.__library.keys():
            if i == char.capitalize():
                return True
        return False

    def doesMorseCodeExist(self, code):
        if code[len(code) - 1] == " ":
            code = code[:len(code)-1]
        for char, morse in morseLibrary().__library.items():
            if morse == code:
                return True
            
        return False

    # Returns the corresponding morse code from a single character
    def returnMorse(self, char):
        
        return morseLibrary.__library.get(char.capitalize())
    
    # Returns the corresponding character from a string of morse
    def returnChar(self, code):

        for char, morse in morseLibrary.__library.items():
            if morse == code:
                return char
        # return None

    # Translates a string to morse
    def translateToMorse(self, sentence):
        
        morse = ""

        for char in sentence:
            if char != " ":
                morse += self.returnMorse(char) + " "
            else:
                morse += "/ "
        return morse

    # Transklates a entire morse code to a spring
    def translateToSentence(self, code):
        if code[len(code) - 1] != " ":
            code += " "
        sentence = ""
        morse = ""

        for char in code:
            
            if char == "/":
                sentence += " "
            elif char == " ":
                if morse != "":
                    sentence += str(self.returnChar(morse))
                    morse = ""
            elif char != " ":
                morse += char
            
        return sentence
