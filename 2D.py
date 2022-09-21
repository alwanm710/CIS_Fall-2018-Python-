ROWS = 2
COLS = 3
values = [[0]* COLS for i in range(ROWS)]
print (values) #Python quick Print
for row in range(0,ROWS): #Pythion no -1
    for col in range(0,COLS):
        values[row][col] =  \
            float(input("Enter a number."))

print(values) #Python quick Print
#Note \ above allows you to break up
#a long line into 2 or multiple lines


#Personal Note:
##ch08_(1).pptx, Slide 31
