__author__ = 'cavanaghb'

from FileAnalyser1 import txtfiles


def selectedfiletype(_selectedfile):   #this is the open file function linked back to the open file button

    if _selectedfile.endswith('.txt'):

        txtfiles.newtxtfiles(_selectedfile)             #create copies of the files
        txtfiles.filedetailstxt(_selectedfile)           #get the file details
        txtfiles.bincontxt(_selectedfile)               #convert to binary
        txtfiles.hexcontxt(_selectedfile)               #convert to hex

    elif _selectedfile.endswith('.bmp'):
        newbinaryfile = open("binaryfilebmp.bmp", 'w+')
        newhexfile = open("hexfilebmp.bmp", 'w+')
