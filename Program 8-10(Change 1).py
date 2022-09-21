#Program 8-10
#SIZE = 5
numbers = [2.5,8.3,6.5,4.0,5.2]
total = 0
for index in range(0,len(numbers)):
    total = total + numbers[index]
average = total/len(numbers)
print("total",total,"average",average)
