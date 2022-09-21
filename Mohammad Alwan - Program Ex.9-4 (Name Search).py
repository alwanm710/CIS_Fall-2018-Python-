#Mohammad Alwan, Program Ex.9-4 (Name Search)

##found = False

def binary_search(arr, value):
    # Set the initial values.
    first = 0 #0 relative array
    last = len(arr) - 1
    position = -1
    found = False
    while not found and first <= last:  
        middle = (first + last) // 2 
        if arr[middle] == value:     
            found = True
            position = middle     
        elif arr[middle] > value: 
            last = middle - 1     
        else:                     
            first = middle + 1    
    return found


numOfNames = int(input('Enter the number of names to be entered.  Max 20 names: '))

NumberOfNames = numOfNames
Names_Plus1 = NumberOfNames + 1
myArray = [""] * Names_Plus1
print("Enter "+str(NumberOfNames)+" names, please.")

for index in range(1,Names_Plus1):
    myArray[index] = str(input("Enter name number "+str(index)+": ").title())

print(myArray)
myArray.sort()
print(myArray)


Search = input("Would you like to search for a name? Y or N? ").lower()
while (Search == "y"):
    SearchName = str(input("Enter a name to search for in the list: ").title())
    if binary_search(myArray, SearchName):
        print ("found",SearchName,"in list")
    else:
        print(SearchName,"isn't found in list")
    Search = input("Would you like to search for another name? Y or N? ").lower()
print("That's all folks")



