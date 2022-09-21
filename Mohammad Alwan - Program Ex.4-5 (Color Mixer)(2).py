#Mohammad Alwan, Program Ex. 4-5 :(Color Mixer)

#Inputs for color1 and color2
Color1 = input('Input color 1: ')
Color1 = Color1.lower()
while Color1 != "red" and Color1 != "yellow" and Color1 != "blue":
    color1 =input("Invalid first color, please enter red yelow or blue: ")

Color2 = input('Input color 2: ')
Color2 = Color2.lower()
while Color2 != "red" and Color2 != "yellow" and Color2 != "blue":
   color2 =input("Invalid second color, please enter red, yelow or blue: ")


#If statement when color inputs are red and blue or blue and red well equal purple
if (Color1 == "red" and Color2 == "blue") or (Color1 == "blue" and Color2 == "red"):
    print('Mixing',Color1,'and',Color2,'make purple')

#If statement when color inputs are red and yellow or yellow and red well equal orange
if (Color1 == "red" and Color2 == "yellow") or (Color1 == "yellow" and Color2 == "red"):
    print('Mixing',Color1,'and',Color2,'make orange')

#If statement when color inputs are yellow and blue or blue and yellow well equal green
if (Color1 == "yellow" and Color2 == "blue") or (Color1 == "blue" and Color2 == "yellow"):
    print('Mixing',Color1,'and',Color2,'make green')

#If statement when both Color1 and Color2 where the same.
if Color1 == Color2:
    print('Super',Color2)

print("Thanks for using the Color Mixer 5000!")
print("Have a good day!")
