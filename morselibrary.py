class morseLibrary:
    __morseLibrary = {
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

    # Returns the corresponding morse code from a single character
    def returnMorse(self, Character):
        
        return morseLibrary.__morseLibrary.get(Character.capitalize())
    
    # Returns the corresponding character from a string of morse
    def returnChar(self, code):

        for char, morse in morseLibrary.__morseLibrary.items():
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

        sentence = ""
        morse = ""

        for char in code:

            
            if char == "/":
                sentence += " "
            elif char == " " and morse != "":
                sentence += str(self.returnChar(morse))
                morse = ""
            elif char != " ":
                morse += char

        return sentence
