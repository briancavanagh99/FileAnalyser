__author__ = 'cavanaghb'

from FileAnalyser1 import txtfiles
from FileAnalyser1 import jpegfiles


def selectedfiletype(_selectedfile):   #this is the open file function linked back to the open file button

    if _selectedfile.endswith('.txt'):

        #txtfiles.newtxtfiles(_selectedfile)             #create copies of the files
        txtfiles.filedetailstxt(_selectedfile)           #get the file details
        txtfiles.bincontxt(_selectedfile)               #convert to binary
        txtfiles.hexcontxt(_selectedfile)               #convert to hex
        txtfiles.uritxt(_selectedfile)
        txtfiles.imagestxt(_selectedfile)
        txtfiles.audiotxt(_selectedfile)
        txtfiles.videotxt(_selectedfile)

'''
    elif _selectedfile.endswith('.jpeg'):
        something

    elif _selectedfile.endswith('.csv'):
        something

    else _selectedfile.endswith('.avi'):
        something
'''