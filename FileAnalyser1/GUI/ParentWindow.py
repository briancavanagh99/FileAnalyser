__author__ = 'cavanaghb'

#file for parent window that all other windows will become a child of

import tkinter


class MainWindow(tkinter.NewMainWindow):

    def __init__(self, parent):
        tkinter.NewMainWindow.__init__(self, parent)              #create the parent window
        self.parent = parent                        #we can keep track of the parent window this way
        self.startapp()

    def startapp(self):
        pass                                    #This is where all my buttons and widgets and such will go


if __name__ == "__main__":
    newapp = MainWindow(None)
    newapp.title('my application')
    newapp.mainloop()

