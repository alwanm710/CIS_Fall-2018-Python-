str="AbCdE"
upperCaseCount=0
for index in range(0,len(str)):
    if str[index].isupper():
        upperCaseCount =upperCaseCount + 1
print(upperCaseCount)
