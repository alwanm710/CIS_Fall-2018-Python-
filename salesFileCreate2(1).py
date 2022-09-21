#Sales with control break logic
from pathlib import Path
from shutil import copyfile
from time import strftime

def is_float(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
    
def makeBackupFile(externalName):
    startFileSuffix = externalName.find(".")
    backupName = externalName[0:startFileSuffix]+strftime("%Y-%m-%d-%H-%M-%S")+ externalName[startFileSuffix:len(externalName)]
    print(backupName,"backup created")
    copyfile(externalName,backupName)

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

stores =['101','102','103','201','202','203','301','302','303']

EXTERNAL_NAME = "sales.dat"

#Check if salesFile already exists and if so user wants to override it
my_file = Path(EXTERNAL_NAME)
if my_file.is_file():
    makeBackup ="" #go through loop first time
    while (makeBackup != "n" and makeBackup != "y"):
           makeBackup = input(EXTERNAL_NAME + " file exists want a backup? enter y or n: ").lower()
    if makeBackup == "y":
           makeBackupFile(EXTERNAL_NAME)
    answer = str.lower(input(str(my_file) + " exists enter 'o' to overwrite or 'a' to append to existing file: "))
    while (answer != "o" and answer != "a"):
        answer = str.lower(input("File exists please enter 'o' to overwite or 'a' to append:"))
    if answer == "o":
       salesFile = open(EXTERNAL_NAME,"w")
    else:
       salesFile = open(EXTERNAL_NAME,"a")
else: #file does not exist
    salesFile = open(EXTERNAL_NAME,"w")

#enter data and write file
print("Below enter your new store data")
print("When done entering all store data enter 0 for store number")
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
print("program ended, may want to verify data in notepad or notepad++")

  
                    
