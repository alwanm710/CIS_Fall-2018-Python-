#Mohammad Alwan, Program Ex.10-1(File Display)

Number = open("numbers.dat","r")
c = Number.readline() #first read
while (c != ""):
      print(c.strip('\n')) # process record
      c = Number.readline()
Number.close()

