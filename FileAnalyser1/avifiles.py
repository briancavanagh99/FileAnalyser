__author__ = 'brian_000'

__author__ = 'cavanaghb'


#conversion file to act as trigger for parent window file to binary


import os
import re
#import binascii


def filedetailscsv(_selectedfile):       #preform file analysis on the original file

    filename = os.path.basename(_selectedfile)          #file name
    filesize = os.path.getsize(_selectedfile)               #file size
    fileextension = ["This is a CSV file"]         #file extension

    filedetailresult = str(filename) + str(filesize) + str(fileextension)        #create a string out of each piece of data and return to the main window
    global _filedetailresult
    _filedetailresult = filedetailresult


def binconcsv(_selectedfile):

    binaryconvert = ' '.join(format(ord(x), 'b') for x in _selectedfile)   #NEED TO CONFIRM THE FULL WORKING OF THIS!!!
    global _binaryresult
    _binaryresult = binaryconvert


def hexconcsv(_selectedfile):
    hexconvert = " ".join(hex(ord(n)) for n in _selectedfile)               #FIGURE OUT THIS LINE FULLY!!!
    global _hexresult
    _hexresult = hexconvert


def uricsv(_selectedfile):                                      #THIS ISNT WORKING NEED TO CONFIRM REGEX SEARCH
    uriresult = re.findall(r'(www?://\S+)', _selectedfile)
    global _uriresult
    _uriresult = uriresult


def imagescsv(_selectedfile):               #CHANGE THIS TO READ AND PRINT CSV DATA
    noimagescsv = ["There are no images in a CSV file"]
    global _imageresult
    _imageresult = noimagescsv


    #def kwiccsv(_selectedfile):            #CAN@T FIND LIBRARY FOR THIS


def audiocsv(_selectedfile):
    noaudiocsv = ["There is audio in a CSV file"]
    global _audioresult
    _audioresult = noaudiocsv


def videocsv(_selectedfile):
    novideocsv = ["There is no video in a CSV file"]
    global _videoresult
    _videoresult = novideocsv





