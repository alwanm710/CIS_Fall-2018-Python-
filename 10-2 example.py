string ="abc"
##for index in range(0,len(string)):
##    if string[index]=="b":
##        string[index]="B"  #gives immutable string error
##print (string)
#so comment out above and first copy string to an array
size = len(string)
array = [" "] * size
for index in range(0,size):
    array[index] = string[index]
for index in range(0,size):
    if array[index] == "b":
        array[index] = array[index].upper()
print(array)
