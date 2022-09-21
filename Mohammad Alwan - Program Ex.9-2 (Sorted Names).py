#Mohammad Alwan, Program Ex.9-2 (Sorted Names)


NumberOfNames = 20
Names_Plus1 = NumberOfNames + 1
myArray = [""] * Names_Plus1
print("Enter 20 names, please.")

for index in range(1,Names_Plus1):
    myArray[index] = str(input("Enter name number "+str(index)+": "))

print(myArray)
myArray.sort()
print(myArray)

