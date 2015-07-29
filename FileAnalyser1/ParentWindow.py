__author__ = 'cavanaghb'

#file for parent window that all other windows will become a child of

import tkinter
from tkinter import filedialog
from FileAnalyser1 import filetype
import tkinter.ttk as ttk



class MainWindow(tkinter.Frame):

    def __init__(self, root):             #first window dialog to open

        tkinter.Frame.__init__(self, root)

        filebutton = tkinter.Button(root, text="Open File for Selection button", width=70, command=self.getfile)
        filebutton.pack()

        quitbutton = tkinter.Button(root, text="Quit", width=70, command=quit)
        quitbutton.pack()

        tab1 = ttk.Frame(newnotebook)
        tab2 = ttk.Frame(newnotebook)
        tab3 = ttk.Frame(newnotebook)

        newnotebook.add(tab1, text="Tab One")
        newnotebook.add(tab2, text="Tab Two")
        newnotebook.add(tab3, text="Tab Three")
        newnotebook.pack()




    def getfile(self):   #this is the open file function linked back to the open file button

        selectedfile = filedialog.askopenfilename(filetypes=[('All files', '*.*')])   #select and open a file
        filetype.selectedfiletype(selectedfile)          #execute the filetype function to confirm file type and start conversion







if __name__=='__main__':
    root = tkinter.Tk()
    newnotebook = ttk.Notebook(root)
    MainWindow(root).pack()
    root.geometry("1000x600+200+50")
    root.title('File Analysis Tool')

    root.mainloop()