__author__ = 'cavanaghb'

#class to open and save the file


def getfile(self):   #this is the open file function

    selectedfile = filedialog.askopenfilename(filetypes=[('All files', '*.*')])  #'selectedfile' is the file as an arguement
    selectedfile = tempfile.TemporaryFile(prefix='tempFATfile', suffix='tmp', dir="C:")
    #print(selectedfile)               #test to confirm creation of tempfile