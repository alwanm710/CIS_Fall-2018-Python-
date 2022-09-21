menuSelection = input("Enter your selection between 1 to 3: ")

while (menuSelection < "1" or menuSelection > "3") or len(menuSelection) > 1:
    print("That is an invalid selection. Please enter 1, 2, or 3.")
    menuSelection = input("Enter your selection between 1 to 3: ")
