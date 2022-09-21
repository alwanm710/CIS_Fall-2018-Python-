fp = open("a.txt","a")
fp.write("three record\n")
fp.write("four record\n")
fp.close()
#do many things with fp
fp = open("a.txt","r")
c = fp.readline() #first read
while (c != ""):
      print(c.strip("\n")) # process record
      c = fp.readline()
fp.close()
