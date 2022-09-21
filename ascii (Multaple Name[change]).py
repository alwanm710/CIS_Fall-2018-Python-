names = ["Bob","Roger"]
for name in names:
    print (name,end="")
    for nextLetter in name: 
        letter = nextLetter
        asciiLetter = ord(letter)
        print(" -",asciiLetter,end="")
    print()
