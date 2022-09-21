from bisect import bisect_left

def binary_search(arr, value):
    # Set the initial values.
    first = 0 #0 relative array
    last = len(arr) - 1
    position = -1
    found = False
    while not found and first <= last:  #if first = last then notfound
        middle = (first + last) // 2 #find middle index - // as index integer :)
        if arr[middle] == value:     #check value for middle index as what you are looking for
            found = True
            position = middle     #save off index that points to hit
        elif arr[middle] > value: # else if value is in the lower half...
            last = middle - 1     # -1 since middle not it
        else:                     # else if value is in the upper half...
            first = middle + 1    # +1 since middle not it
    return found

#main  - note below don't need continuation character for array (Python List) values 
firstNames = ["sahil","mohammad","alan","alex","eric","quinn","will","genna","peter", 
              "juan","thomas","fabian","lucas","michael","jake","brant","eduardo", 
              "christian","paul","mike","jack","jackie","zac"] 
firstNames.sort() #binary search only works on a sorted list
print(firstNames)
searchName = ""
while searchName != "done":
    searchName = input("Enter a name to search for or 'done' to end program:")
    if searchName == "done":
        break
    if binary_search(firstNames,searchName):
        print ("found",searchName,"in array")
    else:
        print(searchName,"not found")

#try Python generic function bisect which gives insertion point to left of duplicates
    
    i = bisect_left(firstNames,searchName)
    print(i) # show index returned by Python bisect_left
    if i < len(firstNames) and firstNames[i] == searchName:
        print(firstNames[i],"found") #return True - if function
    else:
        print(searchName,"not found") #return False 
