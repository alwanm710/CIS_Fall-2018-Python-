import sys

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def MercuryInfo():
    print(" Average dsitance from the sun       57.9 million kilometers    ")
    print(" Mass                                3.31 * 10^23kg             ")
    print(" Surface temperature                 -173 to 430 degrees Celsius")

def VenusInfo():
    print(" Average dsitance from the sun       57.9 million kilometers    ")
    print(" Mass                                3.31 * 10^23kg             ")
    print(" Surface temperature                 -173 to 430 degrees Celsius")

def EarthInfo():
    print(" Average dsitance from the sun       57.9 million kilometers    ")
    print(" Mass                                3.31 * 10^23kg             ")
    print(" Surface temperature                 -173 to 430 degrees Celsius")
    

def MarsInfo():
    print(" Average dsitance from the sun       57.9 million kilometers    ")
    print(" Mass                                3.31 * 10^23kg             ")
    print(" Surface temperature                 -173 to 430 degrees Celsius")
    

def end():
    print("That's all folks")
    sys.exit(0)
    
def printMenu():
    print("1. Mercury............")
    print("2. Venus..............")
    print("3. Earth..............")
    print("4. Mars...............")
    print("5. Exit the program...")



#main

printMenu()
i='0'
while not('1' <= i <= '5' and len(i) == 1):
    choice = input("enter choice from menu above:")
    if choice == '1':
        MercuryInfo()
    elif choice == '2':
        VenusInfo()
    elif choice =='3':
        EarthInfo()
    elif choice == '4':
        MarsInfo()
    elif choice == '5':
        end()        
    else:
        print("number must be between 1 and 5 on menu above")



dictionary = {
        '1': Mercury,
        '2': Venus,
        '3': Earth,
        '4': Mars,
        '5': Exit_the_program
}        
while not ('1' <= i <= '5'):
    choice = input("enter choice from menu above:")
    func = dictionary.get(choice,"ooops")
    if func != "ooops":
        func()
    else:
        print(func, "number must be between 1 and 5 on menu above")




