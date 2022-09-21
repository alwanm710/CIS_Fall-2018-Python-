from tkinter import *
class MPGCalculator:
    def __init__(self):
        def MPGClicked(result,Gallons,Miles):
           result.configure(text = float(Miles.get())/float(Gallons.get()))
        #Create the main window
        self.main_window = Tk()
        #create all widgets
        self.GallonsLabel = Label(self.main_window, \
            text = "Enter the number of gallons the car can hold:")
        self.GallonsEntry = Entry(self.main_window)
        self.MilesLabel = Label(self.main_window, \
            text = "Enter the number of miles the car can be driven on a full tank:")
        self.MilesEntry = Entry(self.main_window)
        self.resultLabel = Label(self.main_window, \
            text = "The MPG is:")
        self.resultAmount = Label(self.main_window, \
            text=" ") # no output to start
        self.MPGButton=Button(self.main_window,text = "Calculate Gross Pay",\
            command=lambda: MPGClicked(self.resultAmount,\
                                        self.GallonsEntry,self.MilesEntry))
        self.exitButton=Button(self.main_window,text= "Exit",\
            command=self.main_window.destroy) 
        #layout screen
        self.GallonsLabel.grid(row=0,column=0) 
        self.GallonsEntry.grid(row=0,column=1) 
        self.MilesLabel.grid(row=1,column=0)
        self.MilesEntry.grid(row=1,column=1)
        self.resultLabel.grid(row=2,column=0)
        self.resultAmount.grid(row=2,column=1)
        self.MPGButton.grid(row=3,column=0)
        self.exitButton.grid(row=3,column=1)
        mainloop()

my_Windows = MPGCalculator()

