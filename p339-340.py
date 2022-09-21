def isInvalid(mode1):
# A local variable to hold True or False.
# If the model number is invalid, set status to True.
# Otherwise, set status to False. (or not(model==100 or model==200 or model==300)
    if model != 100 and model != 200 and model != 300: #DeMorgan 
        status = True
    else:
        status = False
    # Return the test status.
    return status


# MAIN Get the model number.
model = int(input("Enter the model number."))
while isInvalid(model):
    print("The valid model numbers are 100, 200, and 300.")
    model = int(input("Enter the model number."))
                           
