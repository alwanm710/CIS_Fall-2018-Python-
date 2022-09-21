
squareFeetWall = int(input("Enter the Square feet of wall space to be painted: "))
gallonPrice = int(input("Enter price of the paint per gallon: "))

paintRequired = (squareFeetWall / 115)
laborRequired = squareFeetWall / (115 / 8)
costOfPaint = paintRequired * gallonPrice
laberCharge = 20 * laborRequired
totalCostOfPaintJob = laberCharge + costOfPaint

print("The number of gallons required to paint the room is",paintRequired)
print("The hours of labor required is",laborRequired)
print("The cost of the paint is $"+str(costOfPaint))
print("The labor charges is $"+str(laberCharge))
print("The total cost of the paint job is $"+str(totalCostOfPaintJob))
