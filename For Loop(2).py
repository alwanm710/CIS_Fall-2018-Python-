#Python
total = 0
counter = 0
for number in range (1,6,2):
    print(number)
    total = total + number  # total number
    counter = counter + 1  # times through loop
print('loop ', number,' total is now ',total)
print ('times through the loop is ',counter)
