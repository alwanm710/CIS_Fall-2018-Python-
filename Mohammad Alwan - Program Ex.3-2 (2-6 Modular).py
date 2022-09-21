#Mohammad Alwan, Program Ex.3-2 (2-6 Modular)

STATE_TAX_RATE = 0.04
def COMPUTE_STATE_TAX(SALES_PRICE):
    STATE_TAX = STATE_TAX_RATE * SALES_PRICE
    return STATE_TAX

#Main
SALES_PRICE = float(input('Enter the sales price: '))
STATE_TAX = COMPUTE_STATE_TAX(SALES_PRICE)
print(STATE_TAX)
