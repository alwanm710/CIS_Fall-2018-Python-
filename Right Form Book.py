#print(upperCaseCount)
def insert(string1,pos,string2):
   return (string1[0:pos] + string2 + string1[pos:len(string1)])
#main
str="New City"
print(insert(str,4,"York "))
def delete(string,start,end):
    return string[0:start-1] + string[end:len(string)]
print(delete("I ate 1000 blueberries",8,9))
