#Mohammad Alwan, Program Ex.4-6: (Book Club Points)

#Asking to input the number of books bought this month
NumberBooks = int(input('Number of books bought these month: '))
while NumberBooks < 0:
    input("Please enter a postive number or zero.")
    system.out

if NumberBooks == 0:
    Points == 0
elif NumberBooks == 1:
    Points == 5
elif NumberBooks == 2:
    Points == 15
elif NumberBooks == 3:
    Points == 30
else:
    Points == 60

print("You bought",NumberBooks,"of books, so you have",Points,"of points")
