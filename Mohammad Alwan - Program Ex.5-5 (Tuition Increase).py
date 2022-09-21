#Mohammad Alwan, Program Ex.5-5 (Tuition Increase)

#The tuition cost and percentage increase
Tuition = 6000.00
YearlyIncrease = 0.02
numberOfYears = 0

while(numberOfYears < 5):
    IncreaseInTuition = Tuition * YearlyIncrease
    Tuition = Tuition + IncreaseInTuition
    numberOfYears += 1
    print("When it is",numberOfYears,"years from now the tuition will cost $",round(Tuition,2))

