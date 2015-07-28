__author__ = 'cavanaghb'

#file for parent window that all other windows will become a child of

import tkinter
from tkinter import filedialog
import tempfile
import shutil

class mainwindow(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.startapp()

    def startapp(self):
        self.grid()

        filebutton = tkinter.Button(self, text="Open File for Selection button", command=self.getfile)
        filebutton.grid(column=1, row=0)

        quitbutton = tkinter.Button(self, text="Quit", command=quit)
        quitbutton.grid(column=2, row=0)

        self.grid_columnconfigure(0, weight=1)

    def getfile(self):   #this is the open file function

        selectedfile = filedialog.askopenfilename(filetypes=[('All files', '*.*')])
        temp = tempfile.TemporaryFile()
        temp.write(selectedfile)

        print(selectedfile)               #test to confirm creation of tempfile


if __name__ == "__main__":
    NewWindow = mainwindow(None)
    NewWindow.geometry("1000x600+200+50")
    NewWindow.title('File Analysis Tool')
    NewWindow.mainloop()