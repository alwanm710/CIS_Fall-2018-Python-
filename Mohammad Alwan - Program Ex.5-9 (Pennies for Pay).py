#Mohammad Alwan, Program Ex.5-9 (Pennies for Pay)

NumberOfDays = int(input("Enter number of days: "))
AmountOfPennys = 0.01
Days = 0

while Days < NumberOfDays:
    Days += 1
    print("On day",Days,"your salary well be $",AmountOfPennys,)
    AmountOfPennys = AmountOfPennys * 2
print("Your Total salary for",NumberOfDays,"days is $"+str(AmountOfPennys/2))
