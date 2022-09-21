number = int(input(' enter your first number '))
min = number
max = number
i = 0
while number != -99 :
        if number > max :
                max = number
        if number < min :
                min = number
        i=i+1
        print ('number ',i,' = ', number)
        number = int(input(' enter next number or -99 to signal end of input '))
print (' of the numbers above, the max is ', max, ' and the min is ',min)
