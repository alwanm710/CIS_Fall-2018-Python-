#Loops to process files
salesFile = open("sales.dat","w")
numDays = 3
for counter in range (1,numDays+1):
    sales = float(input("Enter sales for day #" \
                      + str(counter) +" :"))
    salesFile.write(str(sales)+'\n') # with newline 

salesFile.close()
salesFile = open("sales.dat","a")
sales = float(input("Append another sale:"))
salesFile.write(str(sales)+'\n') # with newline
salesFile.close()

salesFile = open("sales.dat","r")
salesFileEOF = False
while not(salesFileEOF):
    sales = salesFile.readline()
    if sales == "": #signals EOF
        salesFileEOF = True
    else:
        print(sales,end="")
