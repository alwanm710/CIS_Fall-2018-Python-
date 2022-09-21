SIZE = 100
values=[" "] * SIZE
count = 0


number = input("Enter a letter, or -1 to quit.")

while (number != "-1" and count < SIZE):
     values[count] = number
     count = count + 1
     number = input("Enter a letter, or -1 to quit.")
   
               
print("Here are the values you entered:")
for index in range (0,count):
     print(values[index])
print(values)


#Personal Note:
##ch08_(1).pptx, Slide 20
