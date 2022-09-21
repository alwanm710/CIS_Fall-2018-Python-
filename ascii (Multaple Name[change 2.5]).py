SIZE = 25 #max class size + 1
names=[" "] * SIZE

fileOfNames = open("D:/CIS - Fall-2018/ClassFirstNames.txt","r")

## Get names from file
for index in range(SIZE):
    nextName = fileOfNames.readline()
    if nextName == "":  #then at EOF End Of File
        break
    else:
        names[index] = nextName
fileOfNames.close() #close file when done using it
numberOfNames = index # don't subtract one as counting from 1
print(names)
print("number in class is",numberOfNames)
#get ascii
for index in range(0,numberOfNames):
    name=names[index]
    print (name.strip('\n')," -- ",end="")
    for nextLetter in name: 
        letter = nextLetter
        asciiLetter = ord(letter)
        print(asciiLetter,"-",end="")
    print("")
