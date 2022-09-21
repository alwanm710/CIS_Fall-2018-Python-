# 4.8 Python semulate case with if and elif
modelNumber = int(input("enter Model number 100,200 or 300 "))

model_100_size = 100
model_200_size = 200
model_300_size = 300

model_100_price = 10.00
model_200_price = 20.00
model_300_price = 30.00
                  
if modelNumber == 100:
    print("Price: $" + str(model_100_price)) #ENDL is default of Python print
    print("Size:", model_100_size)
elif modelNumber == 200:
    print("Price: $" + str(model_200_price)) #ENDL is default of Python print
    print("Size:", model_200_size)
elif modelNumber == 300:
    print("Price: $" + str(model_300_price)) #ENDL is default of Python print
    print("Size:", model_300_size)
else:
    print("Invalid model number.")
    
