import sys

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def inchesToCentimeters():
    inches = input("Enter number of inches:")
    while not (is_float(inches)):
        print ("Input must be a real number")
        inches = input("Enter number of inches:")
    centimeters =float(inches)*2.54
    print (inches, "inches is",centimeters,"centimeters")

def feetToMeters():
    feet = input("Enter number of feet:")
    while not (is_float(feet)):
        print ("Input must be a real number")
        feet = input("Enter number of feet:")
    meters =float(feet)*0.3048
    print (feet, "feet is",meters,"meters")

def milesToKilometers():
    miles = input("Enter number of miles:")
    while not (is_float(miles)):
        print ("Input must be a real number")
        miles = input("Enter number of miles:")
    kilometers =float(miles)*1.609
    print (miles, "miles is",kilometers,"kilometers")

def end():
    print("that's all folks")
    sys.exit(0)
    
def printMenu():
    print("1. Convert inches to Centimeters")
    print("2. Convert feet to Meters.......")
    print("3. Convert miles to Kilometers..")
    print("4. exit program")    



#main

printMenu()
i='0'
while not('1' <= i <= '4' and len(i) == 1):
    choice = input("enter choice from menu above:")
    if choice == '1':
        inchesToCentimeters()
    elif choice == '2':
        feetToMeters()
    elif choice =='3':
        milesToKilometers()
    elif choice == '4':
        end()        
    else:
        print("number must be between 1 and 4 on menu above")



##dictionary = {
##        '1': inchesToCentimeters,
##        '2': feetToMeters,
##        '3': milesToKilometers,
##        '4': end
##}        
##while not ('1' <= i <= '4'):
##    choice = input("enter choice from menu above:")
##    func = dictionary.get(choice,"ooops")
##    if func != "ooops":
##        func()
##    else:
##        print(func, "number must be between 1 and 4 on menu above")
##
