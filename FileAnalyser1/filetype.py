__author__ = 'cavanaghb'

from FileAnalyser1 import txtfiles


def selectedfiletype(_selectedfile):   #this is the open file function linked back to the open file button

    if _selectedfile.endswith('.txt'):

        txtfiles.newtxtfiles(_selectedfile)
        txtfiles.filedetailstxt(_selectedfile)           #get the file details



    elif _selectedfile.endswith('.bmp'):
        newbinaryfile = open("binaryfilebmp.bmp", 'w+')
        newhexfile = open("hexfilebmp.bmp", 'w+')
