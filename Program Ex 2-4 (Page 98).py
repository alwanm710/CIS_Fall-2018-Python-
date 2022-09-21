#Program Ex 2-4 page, 98

#Sales Tax rate
SALES_TAX_RATE = 0.06

#Geat the price of the 5 items
Item1 = float(input("Enter price of Item 1: "))
Item2 = float(input("Enter price of Item 2: "))
Item3 = float(input("Enter price of Item 3: "))
Item4 = float(input("Enter price of Item 4: "))
Item5 = float(input("Enter price of Item 5: "))
#print (Item1,Item2,Item3,Item4,Item5)

#Computation Subtotal of all items purchased
Subtotal = Item1 + Item2 + Item3 + Item4 + Item5

#Compute Sale Tax
SalesTax = Subtotal * SALES_TAX_RATE

#Compute Total sale = Subtotal + Tax
TotalPrice = Subtotal + SalesTax

#Output the Subtotal, SalesTax, and TotalPrice
print ("Subtotal is", Subtotal, "sales tax is", SalesTax, "total price is", TotalPrice)
