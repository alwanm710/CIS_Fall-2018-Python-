from tkinter import *
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False  

def setUp():
    entryLabel.grid(row=0,column=0)
    entryBox.grid(row=0,column=1)
    entryBox.delete(0,END)
    outputLabel.grid(row=1,column=0)
    convertButton.grid(row=0,column=2)
    outputAnswer.config(text=" ")
    outputAnswer.grid(row=1,column=1)
    
def convertButtonClicked(conversionFactor,inputBox,outputA):
    #check input for float
    print(inputBox.get())
    if is_float(inputBox.get()):
        outputA.config(text=str('{:,.2f}'.format(float(inputBox.get())*conversionFactor))
                                )
    else:    
        outputA.config(text="input not float - try again")

def inchesToCentimeters():  #use global of tkinter objects to save time :)
    entryLabel.config(text="Enter number of inches:")
    outputLabel.config(text="number of centimeters:")
    convertButton.config(command=lambda: convertButtonClicked(2.54,entryBox,outputAnswer))
    setUp()
    
def feetToMeters():
    entryLabel.config(text="Enter number of feet:")
    outputLabel.config(text="number of meters is:")
    convertButton.config(command=lambda: convertButtonClicked(.3048,entryBox,outputAnswer))
    setUp()
    
def milesToKilometers():
    entryLabel.config(text="Enter number of miles:")
    outputLabel.config(text="number of kilometers:")
    convertButton.config(command=lambda: convertButtonClicked(1.609,entryBox,outputAnswer))
    setUp()
    
root = Tk() #set up root as the main window
menuBar = Menu(root) #add menubar in window
root.config(menu=menuBar) #assign menuBar to window
filemenu = Menu(menuBar) # add a submenu to the menuBar 
menuBar.add_cascade(label="Menu", menu=filemenu) #that cascades or pulldown menu
filemenu.add_command(label="1. Convert inches to Centimeters", command=inchesToCentimeters)
filemenu.add_command(label="2. Convert feet to Meters.......", command=feetToMeters)
filemenu.add_command(label="3. Convert miles to Kilometers..", command=milesToKilometers)
filemenu.add_separator() #draws a line that separates menu from options
filemenu.add_command(label="Exit", command=root.destroy) #don't like that word destroy

entryLabel = Label(root)          #set up but don't display 
entryBox = Entry(root)            #until menu selected
outputLabel = Label(root)
outputAnswer = Label(root)
convertButton = Button(root,text="convert")

mainloop()

