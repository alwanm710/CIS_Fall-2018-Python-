# logical constants

time = int(input("enter time as integer 24 \ hour clock: "))

if time > 12:
    isLunchTime = True
else:
    isLunchTime = False

print (isLunchTime)
print ((time > 12))
