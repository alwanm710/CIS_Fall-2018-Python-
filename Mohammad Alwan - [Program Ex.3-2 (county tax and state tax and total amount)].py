#Mohammad Alwan

STATE_TAX_RATE = 0.04
COUNTY_TAX_RATE = 0.02

def computeStateTax(p):
    stateTax = STATE_TAX_RATE * p
    return stateTax

def computeCountyTax(p):
    countyTax = COUNTY_TAX_RATE * p
    return countyTax

def computeTotalPrice(p,t):
    totalPrice = p + t
    return totalPrice



#Main
salesPrice = float(input('Enter the sales price: '))
stateTax = computeStateTax(salesPrice)
countyTax = computeCountyTax(salesPrice)
print(stateTax)
print(countyTax)
totalTax = stateTax + countyTax
print(totalTax)
fullAmount = computeTotalPrice(salesPrice,totalTax)
print("Amount owed",fullAmount)
