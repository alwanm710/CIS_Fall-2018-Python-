SALES_TAX_RATE = 0.07
TIP_RATE = 0.20

def computeMealCost():
    mealCost = float(input('How much did your meal cost? '))
    mealTax = mealCost * SALES_TAX_RATE
    mealTip = (mealCost + mealTax) * TIP_RATE  #20% TIP_RATE add after tax or before tax?
    total = mealCost + mealTax + mealTip
    print("Your meal cost:..$" + format(mealCost,'>10.2f'))
    print("Your tax:....... $" + format(mealTax,'>10.2f'))
    print("Your tip:....... $" + format(mealTip,'>10.2f'))
    print("                  ----------")
    print("Your total:......$" + format(total,'>10.2f'))

computeMealCost()    
