#Mohammad Alwan, Program Ex.8-3 (RainFall Statistics)

Months = 12
Months_Plus1 = Months + 1
myArray = [0.0] * Months_Plus1
print("Enter the total numbers of rainfall for each month")
for index in range(1,Months_Plus1):
    myArray[index] = float(input("Enter total numbers of rainfall for month "+str(index)+": "))
lowest = myArray[1]
highest = myArray[1]
total = myArray[1]
for index in range(2,Months_Plus1):
    total = total + myArray[index]
    if myArray[index] < lowest:
        lowest = myArray[index]
    if myArray[index] > highest:
        highest = myArray[index]
average = total / Months
print("Total is",total,"highest is",highest,"lowest is",lowest,"average is ",format(average,">.2f"))
