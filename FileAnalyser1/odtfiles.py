__author__ = 'brian_000'
__author__ = 'cavanaghb'


#conversion file to act as trigger for parent window file to binary


import os
import re
#import binascii

def filedetailsdoc(_selectedfile):       #preform file analysis on the original file

    filename = os.path.basename(_selectedfile)          #file name
    filesize = os.path.getsize(_selectedfile)               #file size
    fileextension = ["This is a doc file, it can be opened as a word or openoffice document"]

    docdetailresult = str(filename) + str(filesize) + str(fileextension)        #create a string out of each piece of data and return to the main window
    global _filedetailresult
    _filedetailresult = docdetailresult


def bincondoc(_selectedfile):

    binaryconvert = ' '.join(format(ord(x), 'b') for x in _selectedfile)   #NEED TO CONFIRM THE FULL WORKING OF THIS!!!
    global _binaryresult
    _binaryresult = binaryconvert


def hexcondoc(_selectedfile):
    hexconvert = " ".join(hex(ord(n)) for n in _selectedfile)               #FIGURE OUT THIS LINE FULLY!!!
    global _hexresult
    _hexresult = hexconvert


def uridoc(_selectedfile):                                      #THIS ISNT WORKING NEED TO CONFIRM REGEX SEARCH
    uriresult = re.findall(r'(www?://\S+)', _selectedfile)
    global _uriresult
    _uriresult = uriresult


def imagesdoc(_selectedfile):
    noimagesdoc = ["There are no images in a doc file"]
    global _imageresult
    _imageresult = noimagesdoc


    #def kwicdoc(_selectedfile):            #CAN'T FIND LIBRARY FOR THIS


def audiodoc(_selectedfile):
    noaudiodoc = ["There is audio in a doc file"]
    global _audioresult
    _audioresult = noaudiodoc


def videodoc(_selectedfile):
    novideodoc = ["There is no video in a doc file"]
    global _videoresult
    _videoresult = novideodoc




