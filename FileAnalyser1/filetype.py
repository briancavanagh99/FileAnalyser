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


    elif _selectedfile.endswith('.avi'):
        #docfiles.newdocfiles(_selectedfile)             #create copies of the files
        avifiles.filedetailsdoc(_selectedfile)           #get the file details
        _returnfileresult = avifiles._filedetailresult

        avifiles.bincondoc(_selectedfile)               #convert to binary
        _returnbinresult = avifiles._binaryresult

        avifiles.hexcondoc(_selectedfile)               #convert to hex
        _returnhexresult = avifiles._hexresult

        avifiles.uridoc(_selectedfile)
        _returnuriresult = avifiles._uriresult

        avifiles.imagesdoc(_selectedfile)
        _returnimageresult = avifiles._imageresult

        avifiles.audiodoc(_selectedfile)
        _returnaudioresult = avifiles._audioresult

        avifiles.videodoc(_selectedfile)
        _returnvideoresult = avifiles._videoresult

    elif _selectedfile.endswith('.csv'):
        #docfiles.newdocfiles(_selectedfile)             #create copies of the files
        csvfiles.filedetailsdoc(_selectedfile)           #get the file details
        _returnfileresult = csvfiles._filedetailresult

        csvfiles.bincondoc(_selectedfile)               #convert to binary
        _returnbinresult = csvfiles._binaryresult

        csvfiles.hexcondoc(_selectedfile)               #convert to hex
        _returnhexresult = csvfiles._hexresult

        csvfiles.uridoc(_selectedfile)
        _returnuriresult = csvfiles._uriresult

        csvfiles.imagesdoc(_selectedfile)
        _returnimageresult = csvfiles._imageresult

        csvfiles.audiodoc(_selectedfile)
        _returnaudioresult = csvfiles._audioresult

        csvfiles.videodoc(_selectedfile)
        _returnvideoresult = csvfiles._videoresult

    elif _selectedfile.endswith('.jpeg'):
        #docfiles.newdocfiles(_selectedfile)             #create copies of the files
        jpegfiles.filedetailsdoc(_selectedfile)           #get the file details
        _returnfileresult = jpegfiles._filedetailresult

        jpegfiles.bincondoc(_selectedfile)               #convert to binary
        _returnbinresult = jpegfiles._binaryresult

        jpegfiles.hexcondoc(_selectedfile)               #convert to hex
        _returnhexresult = jpegfiles._hexresult

        jpegfiles.uridoc(_selectedfile)
        _returnuriresult = jpegfiles._uriresult

        jpegfiles.imagesdoc(_selectedfile)
        _returnimageresult = jpegfiles._imageresult

        jpegfiles.audiodoc(_selectedfile)
        _returnaudioresult = jpegfiles._audioresult

        jpegfiles.videodoc(_selectedfile)
        _returnvideoresult = jpegfiles._videoresult

