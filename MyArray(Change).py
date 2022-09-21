

Size = 3
Size_Plus1 = Size + 1
myArray = [0.0] * Size_Plus1
print("Enter 3 numbers into myArray")
for index in range(1,Size_Plus1):
    myArray[index] = float(input("Enter number "+str(index)+": "))
lowest = myArray[1]
highest = myArray[1]
total = myArray[1]
for index in range(2,Size_Plus1):
    total = total + myArray[index]
    if myArray[index] < lowest:
        lowest = myArray[index]
    if myArray[index] > highest:
        highest = myArray[index]
average = total / Size
print("Total is",total,"highest is",highest,"lowest is",lowest,"average is ",format(average,">.2f"))
