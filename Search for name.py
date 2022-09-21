names=["roger","claire","sarah"]
SearchName = input("Enter a name to search for in the list")
##if SearchName.lower() in names:
##    print(SearchName,"found in the list")
##else:
##    print(SearchName,"not found in the list")

for index in range(0,len(names)):
    if SearchName.lower() == names[index]:
        print(SearchName,"Found in the list")
    else:
        print(SearchName,"not found in the list")
