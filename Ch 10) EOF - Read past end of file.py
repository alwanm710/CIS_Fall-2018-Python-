fp = open("a.txt","w")
fp.write("one rec")
fp.close()
#do many things with fp
fp = open("a.txt","r")
c=fp.readline() 
print(c)
c = fp.readline()
print (c)
if c is "":  #check null string
    print ('fp is at the eof')
fp.close()
