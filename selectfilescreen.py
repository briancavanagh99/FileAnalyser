__author__ = 'cavanaghb'

from tkinter import *


class selectfile:  # class for first screen

    root = Tk()  # create the object "root" from the constructor Tk(), Tk() is a Tkinter class
    root.geometry("1000x600+200+50") #main box position
    theLabel = Label(root, text="Select Screen")
    theLabel.pack()  # packs the text from the previous line into the screen

    fileselectbox =

    framesize = Frame(height=550, width=950, bd=2, relief=SUNKEN) #internal content frame details
    framesize.pack(fill=X, padx=5, pady=5)






    root.mainloop()  # this keeps the box open and provides the X or minimize





test = selectfile()