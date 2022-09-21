# Program Ex 2-8 page, 99.

# The tax rate and tip rate.
TAX_RATE = 0.07
TIP_RATE = 0.15

# Get the food charges.
Food = float(input("Enter the charge for food: "))

# Calculate the tip.
Tip = Food * TIP_RATE

# Calculate the tax.
Tax = Food * TAX_RATE

# Calculate the total.
Total = Food + Tip + Tax

# Display the tip, tax, and total.
print ("Tip: $",Tip,"Tax: $",Tax,"Total: $",Total)
