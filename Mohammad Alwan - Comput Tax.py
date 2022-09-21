def computeTax(p):  #p is parameter for price
	taxRate =.02
	taxes = taxRate * p
	return taxes
#main() I just make comment so don't have to indent
#myString = input("enter price\n")
#price = int(myString)    #computeTax like int function
price = float(input("enter price\n"))
tax = computeTax(price)
print("tax is ..$"+ format(tax, '>.2f'))

