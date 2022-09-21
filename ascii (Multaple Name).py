names = ["Bob","Roger"]
for name in names:
    print (name)
    for nextLetter in name: 
        letter = nextLetter
        asciiLetter = ord(letter)
        print(asciiLetter)
