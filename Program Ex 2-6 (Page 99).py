# Program Ex 2-6 page, 99.

# The state sales tax and county sales tax.
STATE_SALES_TAX = 0.04
COUNTY_SALES_TAX = 0.02

# Get the amount of a purchase.
Purchase = float(input("Enter amount of the purchase: "))

# Calculate the state sales tax.
STATE_TAX = Purchase * STATE_SALES_TAX

# Calculate the county sales tax.
COUNTY_TAX = Purchase * COUNTY_SALES_TAX

# Calculate the total sales tax.
TOTAL_SALES_TAX = COUNTY_TAX + STATE_TAX

# Calculate the total of the sales.
TOTAL_SALES = Purchase + TOTAL_SALES_TAX

# Display the amount of the purchase, the state sales tax, the county sales tax, the total sales tax, and the total of the sale.
print ("Amount of the purchase: $",Purchase,"State sales tax: $",STATE_TAX,"County sales tax: $",COUNTY_TAX,"Total sales tax: $",TOTAL_SALES_TAX,"Total of the sale: $",TOTAL_SALES)
