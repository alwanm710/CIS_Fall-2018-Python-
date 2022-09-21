#menu with Switch/case statements that we saw earlier
#Python only has dictionary approach which works ok with menus
#when define functions to handle each case
import sys # for sys.exit(0) graceful end anywhere in program

def getValidInteger(l,u,name,enterMessage):   #integer.py Class 8 Notes & Materials
        valid = False; #assume guilty until proven innocent
        while not valid:
            i =input(enterMessage+" between "+str(l)+" and "+str(u)+":")
            try:
                i =int(i)
                isInt = True
            except:
                isInt = False
            if isInt:
               if l <= i <= u:
                   return i
               else:
                   print("Error -", name, "must be between", 1, "and" ,u)
            else:
                print("Oops",i,"is not a valid integer - try again\n")

def is_float(s):  #note could also make get valid float if know range
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

def exit():
    print("that's all folks!") #nice to give personal message at end of program
    sys.exit(0)

def menu():
    print("Enter:")
    print("\t1: convert inches to centimeters")
    print("\t2: convert feet to meters")
    print("\t3: convert miles to kilometers")
    print("\t4: to exit")

# map the inputs to the function blocks
#main
#define dictionary
options = {1 : inchesToCentimeters,
           2 : feetToMeters,
           3 : milesToKilometers,
           4 : exit
           }
menu()
while True:
    choice = getValidInteger(1,4,"choice","Enter your choice 1,2,3 or 4:")
    options[choice]()

