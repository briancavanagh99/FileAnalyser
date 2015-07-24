__author__ = 'cavanaghb'


from tkinter import *
from tkinter import filedialog

class SelectFile:  #class for first screen


        def __init__(self, master):  #this function creates the buttons on the first screen and points the command at the open file function

            self.filebutton = Button(master, text="Open Files for Selection button", command=self.getfile)
            self.filebutton.pack()

            self.quitbutton = Button(master, text="Quit")# command=quit(mainbox))
            self.quitbutton.pack()


        def getfile(self):   #this is the open file function

            selectedfile = filedialog.askopenfilename(filetypes=[('All files', '*.*')])  #'selectedfile' is the file as an arguement
            print(selectedfile)     #REMOVABLE TEST TO CHECK THE FILE OPENS CORRECTLY



#BEGIN - CREATE THE MAIN WINDOW
mainbox = Tk()  # create the object "mainbox" from the constructor Tk(), Tk() is a Tkinter class
mainbox.geometry("1000x600+200+50") #main box position and size
theLabel = Label(mainbox, text="MAIN SELECT FILE SCREEN")
theLabel.pack()  # packs the text from the previous line into the screen
mainbox.title("File Analysis Tool")
getfilebutton = selectfile(mainbox)
#END - CREATE THE MAIN WINDOW


mainbox.mainloop()  # this keeps the box open and provides the X or minimize, needs to be in the same 'def' as 'root'



testrun = selectfile() #THIS IS A TEST RUN OF THIS CLASS