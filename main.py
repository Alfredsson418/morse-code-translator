import morselibrary

morse = morselibrary.morseLibrary()

print(morse.returnMorse("99"))
print(morse.returnChar(".-----"))
print(morse.translateToMorse("hello to "))

# Errorn beror på att self.returnChar ger none (tror jag)
print(morse.translateToSentence(morse.translateToMorse("hello to ")))