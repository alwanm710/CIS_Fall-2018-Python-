color1 =input("enter first primary color - red yelow or blue: ")
color1=color1.lower() # makes all lowercase, e.g. Blue, BLUE, BLue all become blue
while not (color1 == "red" or color1 == "yellow" or color1 == "blue"): #turn if into while
    color1 =input("Invalid first color, please enter red yelow or blue: ") #give user all valid values
    color1=color1.lower() 
    
color2 =input("enter second primary color - red, yelow or blue: ")
color2= color2.lower()
while color2 != "red" and color2 != "yellow" and color2 != "blue":
   color2 =input("Invalid second color, please enter red, yelow or blue: ")
   color2= color2.lower()
   
if color1 == "red" and color2 == "yellow": #red color1 all lower case with yellow
    print ("the result is orange")
elif color2 == "red" and color1 == "yellow": #red color2 all lower case with yellow
    print ("the result is orange")
elif color1 == "red" and color2 == "blue": #red color1 all lower case with blue
    print ("the result is purple")
elif color2 == "red" and color1 == "blue":
    print ("the result is purple")
elif color1 == "yellow" and color2 == "blue": #yellow color1 all lower case with blue
    print ("the result is green")
elif color2 == "yellow" and color1 == "blue": #yellow color2 all lower case with blue
    print ("the result is green")
else: # both valid then both must be same cdoor :)
    print ("the result is double", color1) # colors not invalid so must be same





    





