sentences = str(input("Please enter a couple of sentences: "))
size = len(sentences)
array = [" "]*size

for index in range(0,size):
    array[index] = sentences[index]
periodFlag = True #pretend period found to capitalize first sentence
for index in range(0,size):
    if periodFlag:
        if array[index].isalpha():
            array[index] = array[index].upper()
            periodFlag = False
    if (array[index] == "." or array[index] == "!" or array[index] == "?"):
        periodFlag = True
print("".join(array))
