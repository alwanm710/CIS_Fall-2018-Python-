#Mohammad Alwan, Program Ex.10-2(Item Counter)

Names = open("ClassFirstNames.txt","r")
c = Names.readline() #first read
ItemCounter = 0
while (c != ""):
      ItemCounter = ItemCounter + 1
      print(str(ItemCounter)+'.',c.strip('\n')) # process record
      c = Names.readline()

print("\nNumber of names in the file is "+str(ItemCounter))

