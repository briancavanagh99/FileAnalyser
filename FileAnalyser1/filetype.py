__author__ = 'cavanaghb'

from FileAnalyser1 import txtfiles
from FileAnalyser1 import odtfiles
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



    elif _selectedfile.endswith('.odt') or _selectedfile.endswith('.doc'):
        #docfiles.newdocfiles(_selectedfile)             #create copies of the files
        odtfiles.filedetailsdoc(_selectedfile)           #get the file details
        _returnfileresult = odtfiles._filedetailresult

        odtfiles.bincondoc(_selectedfile)               #convert to binary
        _returnbinresult = odtfiles._binaryresult

        odtfiles.hexcondoc(_selectedfile)               #convert to hex
        _returnhexresult = odtfiles._hexresult

        odtfiles.uridoc(_selectedfile)
        _returnuriresult = odtfiles._uriresult

        odtfiles.imagesdoc(_selectedfile)
        _returnimageresult = odtfiles._imageresult

        odtfiles.audiodoc(_selectedfile)
        _returnaudioresult = odtfiles._audioresult

        odtfiles.videodoc(_selectedfile)
        _returnvideoresult = odtfiles._videoresult


    else _selectedfile.endswith('.avi'):
        avifiles.filedetailstxt(_selectedfile)           #get the file details
        avifiles.bincontxt(_selectedfile)               #convert to binary
        avifiles.hexcontxt(_selectedfile)               #convert to hex
        avifiles.uritxt(_selectedfile)
        avifiles.imagestxt(_selectedfile)
        avifiles.audiotxt(_selectedfile)
        avifiles.videotxt(_selectedfile)

    elif _selectedfile.endswith('.csv'):
        csvfiles.bincontxt(_selectedfile)               #convert to binary
        csvfiles.hexcontxt(_selectedfile)               #convert to hex
        csvfiles.uritxt(_selectedfile)
        csvfiles.imagestxt(_selectedfile)
        csvfiles.audiotxt(_selectedfile)
        csvfiles.videotxt(_selectedfile)

    else _selectedfile.endswith('.jpeg'):
        jpegfiles.bincontxt(_selectedfile)               #convert to binary
        jpegfiles.hexcontxt(_selectedfile)               #convert to hex
        jpegfiles.uritxt(_selectedfile)
        jpegfiles.imagestxt(_selectedfile)
        jpegfiles.audiotxt(_selectedfile)
        jpegfiles.videotxt(_selectedfile)

