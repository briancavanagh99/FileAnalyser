__author__ = 'brian_000'

__author__ = 'cavanaghb'


#conversion file to act as trigger for parent window file to binary


import os
import re
#import binascii


def filedetailsA(_selectedfile):       #preform file analysis on the original file

    filename = os.path.basename(_selectedfile)          #file name
    filesize = os.path.getsize(_selectedfile)               #file size
    fileextension = ["This is a jpeg file"]         #file extension

    filedetailresult = str(filename) + str(filesize) + str(fileextension)        #create a string out of each piece of data and return to the main window
    global _filedetailresult
    _filedetailresult = filedetailresult


def binconjpeg(_selectedfile):

    binaryconvert = ' '.join(format(ord(x), 'b') for x in _selectedfile)   #NEED TO CONFIRM THE FULL WORKING OF THIS!!!
    global _binaryresult
    _binaryresult = binaryconvert


def hexconjpeg(_selectedfile):
    hexconvert = " ".join(hex(ord(n)) for n in _selectedfile)               #FIGURE OUT THIS LINE FULLY!!!
    global _hexresult
    _hexresult = hexconvert


def urijpeg(_selectedfile):                                      #THIS ISNT WORKING NEED TO CONFIRM REGEX SEARCH
    uriresult = re.findall(r'(www?://\S+)', _selectedfile)
    global _uriresult
    _uriresult = uriresult


def imagesjpeg(_selectedfile):               #CHANGE THIS TO READ AND PRINT jpeg DATA
    noimagesjpeg = ["There are no images in a jpeg file"]
    global _imageresult
    _imageresult = noimagesjpeg


    #def kwicjpeg(_selectedfile):            #CAN@T FIND LIBRARY FOR THIS


def audiojpeg(_selectedfile):
    noaudiojpeg = ["There is audio in a jpeg file"]
    global _audioresult
    _audioresult = noaudiojpeg


def videojpeg(_selectedfile):
    novideojpeg = ["There is no video in a jpeg file"]
    global _videoresult
    _videoresult = novideojpeg





