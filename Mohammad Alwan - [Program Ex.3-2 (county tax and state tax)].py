#Mohammad Alwan, Program Ex.3-2 (2-6 Modular)

STATE_TAX_RATE = 0.04
COUNTY_TAX_RATE = 0.02

def computeStateTax(p):
    stateTax = STATE_TAX_RATE * p
    return stateTax

def computeCountyTax(p):
    countyTax = COUNTY_TAX_RATE * p
    return countyTax




#Main
salesPrice = float(input('Enter the sales price: '))
stateTax = computeStateTax(salesPrice)
countyTax = computeCountyTax(salesPrice)
print(stateTax)
print(countyTax)
