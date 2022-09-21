#Sales with control break logic
from pathlib import Path
import sys
def is_float(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

stores =['101','102','103','201','202','203','301','302','303']
#Check if salesFile already exists ande if so user wants to override it
my_file = Path("sales.dat")
if my_file.is_file():
    answer = str.lower(input(str(my_file) + " exists overwrite? y or n:"))
    while (answer != "y" and answer != "n"):
        answer = str.lower(input("Must be y or n - File exists overwrite? y or n:"))
    if answer == "n":
        print("don't remove existing sales.dat file - program terminated")
        sys.exit(0)


#open salesFile for output
salesFile = open("sales.dat","w")

#enter data and write file
print("Below enter your store data")
print("Whern done entering all store data enter 0 for store number")
while True:
    storeNumber = input("Enter store number or 0: ")
    if storeNumber == "0":
        break
    while not(storeNumber in stores):
         storeNumber = input("Invalid - Please enter valid store code: ")
    state = input("Enter state code for store: ")
    while not(state in states):
         state = input("Invalid - Please enter valid state code for store: ")
    sales = input("Enter sales for store: ")
    while not(is_float(sales)):
        sales = input("Sales must be real number try again: ")
    salesFile.write(str(storeNumber)+","+state+","+str(sales)+'\n')
    
#Close file
salesFile.close()

  
                    
