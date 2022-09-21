#Logical operator and early exit

temperature = int(input("input a temperature: "))
minutes = int(input("input minutes "))

#AND example
if temperature < 20 and minutes > 12 :
    print ("The temperature is in the danger zone.")

#OR example
if temperature < 20 or temperature > 100:
    print("The temperature is in the danger zone.")

#NOT example
if not(temperature > 100):
    print("This is below the maximum temperature.")
