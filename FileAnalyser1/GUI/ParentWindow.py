__author__ = 'cavanaghb'

#file for parent window that all other windows will become a child of

import tkinter
from tkinter import filedialog
import tempfile
import binaryconvert
import hexconvert


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


    def getfile(self):   #this is the open file function linked back to the open file button

        selectedfile = filedialog.askopenfilename(filetypes=[('All files', '*.*')])

        if selectedfile.endswith('.txt'):

            newbinaryfile = open('binaryfiletext.txt', 'w+')              #create a new file to transfer the data to
            newhexfile = open('hexfiletext.txt', 'w+')

            newbinaryfile.write(selectedfile)
            newhexfile.write(selectedfile)

            binconvertedfile = binaryconvert.bincon(newbinaryfile)
            hexconvertedfile = hexconvert.hexcon(newhexfile)



        elif selectedfile.endswith('.bmp'):
            newbinaryfile = open(binary)





        #temp = tempfile.TemporaryFile(mode='w')


#Need to create a binary and hex conversion module, this will be used to convert and save the data into the newly created files



if __name__ == "__main__":
    NewWindow = mainwindow(None)
    NewWindow.geometry("1000x600+200+50")
    NewWindow.title('File Analysis Tool')
    NewWindow.mainloop()