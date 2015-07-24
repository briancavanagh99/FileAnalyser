
__author__ = 'cavanaghb'


from tkinter import *

class selectfile:  #class for first screen


        def __init__(self, master):

            self.filebutton = Button(master, text="Open Files for Selection button", command=self.getfile)
            self.filebutton.pack()

            self.quitbutton =
            self.quitbutton.pack()



        def getfile(self):

            Button = askopenfilename(title="choose your file", filetypes=[("jpeg files", "*.jpg"), ("all files", "*.*")])


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