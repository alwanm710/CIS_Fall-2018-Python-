#menu with Switch/case statements that we saw earlier
#Python only has dictionary approach which works ok with menus
#when define functions to handle each case
import sys

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
def one():
    print ("handle case 1")

def two():
    print ("handle case 2")

def three(): 
    print ("handle case 3")

def exit():
    sys.exit(0)

def menu():
    print("Enter:")
    print("\t1: to do thing 1")
    print("\t2: to do thing 2")
    print("\t3: to do thing 3")
    print("\t4: to exit")

# map the inputs to the function blocks
#main
#define dictionary
options = {1: one,
           2 : two,
           3 : three,
           4 : exit
           }
menu()
while True:
    choice = getValidInteger(1,4,"choice","Enter your choice 1,2,3 or 4:")
    options[choice]()

