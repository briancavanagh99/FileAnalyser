__author__ = 'cavanaghb'

#file for parent window that all other windows will become a child of

import tkinter
from tkinter import filedialog
from FileAnalyser1 import filetype
import tkinter.ttk as ttk
from FileAnalyser1 import txtfiles
import tkinter.scrolledtext


class MainWindow(tkinter.Frame):

    def __init__(self, root):             #first window dialog to open

        tkinter.Frame.__init__(self, root)

        filebutton = tkinter.Button(root, text="Open File for Selection button", width=70, command=self.getfile)
        filebutton.pack()

        quitbutton = tkinter.Button(root, text="Quit", width=70, command=quit)
        quitbutton.pack()



    def getfile(self):   #this is the open file function linked back to the open file button

        selectedfile = filedialog.askopenfilename(filetypes=[('All files', '*.*')])   #select and open a file
        global _selectedfile                    #make the arguement global for use outside the module
        _selectedfile = selectedfile
        filetype.selectedfiletype(_selectedfile)          #execute the filetype function to confirm file type and start conversion



        #Tabs placed here to popup after file selection

        tab1 = ttk.Frame(newnotebook, width=900, height=500)
        results1 = ttk.Label(tab1, text=filetype._returnfileresult)
        results1.pack()


        tab2 = ttk.Frame(newnotebook, width=900, height=500)
        results2 = ttk.Label(tab2, text=filetype._returnbinresult)
        results2.pack()

        newscrollbar = tkinter.Scrollbar(tab2)
        newscrollbar.pack(side='right', fill='y')

        results2 = tkinter.Text(tab2, wrap='word')
        results2.pack()

        results2.config(yscrollcommand=newscrollbar.set)
        newscrollbar.config(command=results2.yview)


        tab3 = ttk.Frame(newnotebook, width=900, height=500)
        results3 = ttk.Label(tab3, text=filetype._returnhexresult)
        results3.pack()

        newscrollbar = tkinter.Scrollbar(tab3)
        newscrollbar.pack(side='right', fill='y')

        results3 = tkinter.Text(tab3, wrap='word')
        results3.pack()

        results3.config(yscrollcommand=newscrollbar.set)
        newscrollbar.config(command=results2.yview)


        tab4 = ttk.Frame(newnotebook, width=900, height=500)
        results4 = ttk.Label(tab4, text=filetype._returnuriresult)
        results4.pack()

        tab5 = ttk.Frame(newnotebook, width=900, height=500)
        results5 = ttk.Label(tab5, text=filetype._returnimageresult)
        results5.pack()


        tab6 = ttk.Frame(newnotebook, width=900, height=500)
        results6 = ttk.Label(tab6, text=filetype._returnaudioresult)
        results6.pack()

        tab7 = ttk.Frame(newnotebook, width=900, height=500)
        results7 = ttk.Label(tab7, text=filetype._returnvideoresult)
        results7.pack()




        newnotebook.add(tab1, text="File Details")
        newnotebook.add(tab2, text="Raw Binary")
        newnotebook.add(tab3, text="Raw Hex")
        newnotebook.add(tab4, text="URI's")
        newnotebook.add(tab5, text="Images")
        newnotebook.add(tab6, text="Audio")
        newnotebook.add(tab7, text="Video")

        newnotebook.pack()


if __name__=='__main__':            #run the main instance to start the program
    root = tkinter.Tk()
    newnotebook = ttk.Notebook(root)
    MainWindow(root).pack()
    root.geometry("1000x600+200+50")
    root.title('File Analysis Tool')

    root.mainloop()