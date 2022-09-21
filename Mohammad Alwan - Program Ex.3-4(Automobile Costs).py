
loanPayment = int(input("What is your monthly loan payment? "))
Insurance = int(input("What is your monthly insurance cost? "))
Gas = int(input("What is your monthly gas cost? "))
Oil = int(input("What is your monthly oil cost? "))
Tires = int(input("What is your monthly tires cost? "))
Maintenance = int(input("What is your monthly maintenance cost? "))

totalMonthlyCost = loanPayment + Insurance + Gas + Oil + Tires + Maintenance
print("Your total monthly cost expenses is $"+str(totalMonthlyCost))

totalAnnualCost = totalMonthlyCost * 12
print("Your total annual cost expenses is $"+str(totalAnnualCost))
