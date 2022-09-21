from tkinter import *
class NameAndAddress:
    def __init__(self):
        #Create the main window
        self.main_window = Tk()

        def showInfoClicked(result):
               result.configure(text = "Mohammad Alwan\n 916 hahn Pl.\n West Chicago, IL 60185")
               
        self.showInfo = Label(self.main_window, \
            text=" ") # no output to start
        self.showInfoButton = Button(self.main_window,text = "Show Info",\
                command = lambda: showInfoClicked(self.showInfo))
        self.exitButton = Button(self.main_window,text = "Exit",\
                command = self.main_window.destroy)
        self.exitButton.grid(row=2,column=1)
        self.showInfoButton.grid(row=2,column=2)
        self.showInfo.grid(row=0,column=1)
                                     
Window = NameAndAddress()
                                     
