fp = open("a.txt","w")
fp.write("one record\n")
fp.write("two record\n")
fp.close()
#do many things with fp
fp = open("a.txt","r")
c = fp.readline() #first read
while (c != ""):
      print(c.strip("\n")) # process record
      c = fp.readline()
fp.close()
