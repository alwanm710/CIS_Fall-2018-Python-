#Program 7-2 (retail.py) 336-337 book
# This program calculates retail prices.
 
# MARK_UP is used as a global constant for
# the markup up percentage.
MARK_UP = 2.5
 
# The main function
def main():
    # Variable to control the loop.
    another = 'y'
     
    # Process one or more items.
    while another.lower() == 'y' :  #another way for another to check 'y' and 'Y'
        # Display an item's retail price.
        show_retail()
         
        # Do this again?
        another = input('Do you have another item? ' +
        '(Enter y for yes): ')
        
#isInteger functions checks a string to see if a valid integer
def isFloat(f):
    try:
        f = float(f) #if this works is an integer
        return True
    except: # except catches bad error and gives contro to programmer
        return False
 
# The show_retail function gets an item's wholesale
# cost and displays the item's retail price.
def show_retail():
    # Get the item's wholesale cost.
    validInput = False
    # Validate the wholesale cost.
    while not(validInput):
        wholesale = input("Enter the item's wholesale cost:$ ")
        if isFloat (wholesale):
           wholesale = float(wholesale)
           if wholesale < 0:
               print('ERROR: the cost must be positive integer - try again')
           else:
               validInput = True
        else:
            print('Error not a valid number for wholesale amount - try again')
         
    # Calculate the retail price.
    retail = wholesale * MARK_UP
     
    # Display the retail price.
    print('The retail price is $', format(retail, '.2f'))
 
# Call the main function.
main()
