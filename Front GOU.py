#Hello GUI
from tkinter import *
class MyGUI:
  def __init__(self): 
      #Create the main window
      self.main_window = Tk() 
      #create label hello widget
      self.label = Label(self.main_window, \
                             text = "Hello World")
      self.label.pack() 
      mainloop()
gui = MyGUI()
