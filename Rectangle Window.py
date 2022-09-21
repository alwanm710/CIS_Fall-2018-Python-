from tkinter import *
def calcAreaButtonClicked(outputLabel,length,width):
    l=int(length.get())
    w=int(width.get())
    outputLabel.configure(text= str(l*w))
#main
main_window = Tk() #main_window is GUI window – close, closes all widgets
lengthLabel=Label(main_window, \
             text="Enter Rec length").grid(row=0,column=0)
widthLabel=Label(main_window, \
             text="Enter Rec width").grid(row=1,column=0)
length = Entry(main_window)
width = Entry(main_window)
length.grid(row=0, column=1)
width.grid(row=1, column=1)
lbl = Label(main_window,text=" ") #what about ouput?
lbl.grid(row=4,column=2)
btn=Button(main_window,text= "Calculate Area",\
command=lambda: calcAreaButtonClicked(lbl,length,width))
btn.grid(row=4,column=1)
quitBtn=Button(main_window,text="Quit",\
               command=main_window.destroy) 
quitBtn.grid(row=5,column=3) #above method call no ()
main_window.mainloop( )
