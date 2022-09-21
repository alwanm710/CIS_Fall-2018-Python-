def parseRecord(rec):
    #parse record
    i=0 
    j=line.find(",",i)
    storeNumber = line[i:j]       # goes from 0 up to comma
    i=j+1 #character after comma
    j=line.find(",",i)  # find next comma
    state =line[i:j] # pull out state
    i=j+1
    sales = float(line[i:len(line)-1]) # get sales and -1 strip off the \n
    return storeNumber,state,sales

salesFile=open("sales.dat","r") #make small sales.dat with notepad
line = salesFile.readline() #first read outside loop
storeNumber,state,sales = parseRecord(line)
print(storeNumber,state,sales)
