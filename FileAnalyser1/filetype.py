__author__ = 'cavanaghb'

from FileAnalyser1 import txtfiles
from FileAnalyser1 import jpegfiles


def selectedfiletype(_selectedfile):   #this is the open file function linked back to the open file button

    if _selectedfile.endswith('.txt'):

        #txtfiles.newtxtfiles(_selectedfile)             #create copies of the files
        txtfiles.filedetailstxt(_selectedfile)           #get the file details
        global _returnfileresult
        _returnfileresult = txtfiles._filedetailresult

        txtfiles.bincontxt(_selectedfile)               #convert to binary
        global _returnbinresult
        _returnbinresult = txtfiles._binaryresult

        txtfiles.hexcontxt(_selectedfile)               #convert to hex
        global _returnhexresult
        _returnhexresult = txtfiles._hexresult

        txtfiles.uritxt(_selectedfile)
        global _returnuriresult
        _returnuriresult = txtfiles._uriresult

        txtfiles.imagestxt(_selectedfile)
        global _returnimageresult
        _returnimageresult = txtfiles._noimagetxt

        txtfiles.audiotxt(_selectedfile)
        global _returnaudioresult
        _returnaudioresult = txtfiles._noaudiotxt

        txtfiles.videotxt(_selectedfile)
        global _returnvideoresult
        _returnvideoresult = txtfiles._novideotxt

'''
    elif _selectedfile.endswith('.csv'):
        csvfiles.filedetailstxt(_selectedfile)           #get the file details
        csvfiles.bincontxt(_selectedfile)               #convert to binary
        csvfiles.hexcontxt(_selectedfile)               #convert to hex
        csvfiles.uritxt(_selectedfile)
        csvfiles.imagestxt(_selectedfile)
        csvfiles.audiotxt(_selectedfile)
        csvfiles.videotxt(_selectedfile)



    elif _selectedfile.endswith('.jpeg'):
        something

    else _selectedfile.endswith('.avi'):
        something
'''