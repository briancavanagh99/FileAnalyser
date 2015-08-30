__author__ = 'cavanaghb'

from FileAnalyser1 import txtfiles
from FileAnalyser1 import docfiles
from FileAnalyser1 import jpegfiles


def selectedfiletype(_selectedfile):   #this is the open file function linked back to the open file button

    global _returnfileresult
    global _returnbinresult
    global _returnhexresult
    global _returnuriresult
    global _returnimageresult
    global _returnaudioresult
    global _returnvideoresult

    if _selectedfile.endswith('.txt'):

        #txtfiles.newtxtfiles(_selectedfile)             #create copies of the files
        txtfiles.filedetailstxt(_selectedfile)           #get the file details
        _returnfileresult = txtfiles._filedetailresult

        txtfiles.bincontxt(_selectedfile)               #convert to binary
        _returnbinresult = txtfiles._binaryresult

        txtfiles.hexcontxt(_selectedfile)               #convert to hex
        _returnhexresult = txtfiles._hexresult

        txtfiles.uritxt(_selectedfile)
        _returnuriresult = txtfiles._uriresult

        txtfiles.imagestxt(_selectedfile)
        _returnimageresult = txtfiles._imageresult

        txtfiles.audiotxt(_selectedfile)
        _returnaudioresult = txtfiles._audioresult

        txtfiles.videotxt(_selectedfile)
        _returnvideoresult = txtfiles._videoresult



    elif _selectedfile.endswith('.odt'):
        #docfiles.newdocfiles(_selectedfile)             #create copies of the files
        docfiles.filedetailsdoc(_selectedfile)           #get the file details
        _returnfileresult = docfiles._filedetailresult

        docfiles.bincondoc(_selectedfile)               #convert to binary
        _returnbinresult = docfiles._binaryresult

        docfiles.hexcondoc(_selectedfile)               #convert to hex
        _returnhexresult = docfiles._hexresult

        docfiles.uridoc(_selectedfile)
        _returnuriresult = docfiles._uriresult

        docfiles.imagesdoc(_selectedfile)
        _returnimageresult = docfiles._imageresult

        docfiles.audiodoc(_selectedfile)
        _returnaudioresult = docfiles._audioresult

        docfiles.videodoc(_selectedfile)
        _returnvideoresult = docfiles._videoresult

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