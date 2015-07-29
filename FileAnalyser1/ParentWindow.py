__author__ = 'cavanaghb'

#file for parent window that all other windows will become a child of

import tkinter
from tkinter import filedialog


class MainWindow(tkinter.Tk):           #main opening window

    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.startapp()



    def startapp(self):             #first window dialog to open
        self.grid()

        filebutton = tkinter.Button(self, text="Open File for Selection button", width=500, command=self.FileOpen.getfile)
        filebutton.grid(column=0, row=0)

        quitbutton = tkinter.Button(self, text="Quit", width=500, command=quit)
        quitbutton.grid(column=1, row=0)

        self.grid_columnconfigure(0, weight=1)




    def getfile(self):   #this is the open file function linked back to the open file button

        selectedfile = filedialog.askopenfilename(filetypes=[('All files', '*.*')])


        if selectedfile.endswith('.txt'):

            newbinaryfile = open('binaryfiletext.txt', 'w+')              #create a new file to transfer the data to
            newhexfile = open('hexfiletext.txt', 'w+')

            newbinaryfile.write(selectedfile)
            newhexfile.write(selectedfile)          #transfer the data to the new files and then convert to hex




        elif selectedfile.endswith('.bmp'):
            newbinaryfile = open("binaryfilebmp.bmp", 'w+')
            newhexfile = open("hexfilebmp.bmp", 'w+')





        #temp = tempfile.TemporaryFile(mode='w')


#Need to create a binary and hex conversion module, this will be used to convert and save the data into the newly created files

#def #TAB screen for binary


#def #TAB screen for hex


#def #screen for file analysis breakdown


#def #screen for searching data in file


#def #Screen n.....



if __name__ == "__main__":                  #mainwindow app start
    root = MainWindow(None)
    root.geometry("1000x600+200+50")
    root.title('File Analysis Tool')
    root.mainloop()