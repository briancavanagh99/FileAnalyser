__author__ = 'cavanaghb'


#conversion file to act as trigger for parent window file to binary


import os
import re
#import binascii

#def newtxtfiles(_selectedfile):
    #newbinaryfile = open('binaryfiletext.txt', 'w+')              #create a new file to transfer the data to
    #newhexfile = open('hexfiletext.txt', 'w+')

    #newbinaryfile.write(_selectedfile)
    #newhexfile.write(_selectedfile)          #transfer the data to the new files


def filedetailstxt(_selectedfile):       #preform file analysis on the original file

    filename = os.path.basename(_selectedfile)          #file name
    filesize = os.path.getsize(_selectedfile)               #file size
    fileextension = ["This is a text file, find out more information about '*.txt' files at", ]         #file extension

    txtdetailresult = str(filename) + str(filesize) + str(fileextension)        #create a string out of each piece of data and return to the main window
    global _filedetailresult
    _filedetailresult = txtdetailresult


def bincontxt(_selectedfile):

    binaryconvert = ' '.join(format(ord(x), 'b') for x in _selectedfile)   #NEED TO CONFIRM THE FULL WORKING OF THIS!!!
    global _binaryresult
    _binaryresult = binaryconvert


def hexcontxt(_selectedfile):
    hexconvert = " ".join(hex(ord(n)) for n in _selectedfile)               #FIGURE OUT THIS LINE FULLY!!!
    global _hexresult
    _hexresult = hexconvert


def uritxt(_selectedfile):                                      #THIS ISNT WORKING NEED TO CONFIRM REGEX SEARCH
    uriresult = re.findall(r'(www?://\S+)', _selectedfile)
    global _uriresult
    _uriresult = uriresult


def imagestxt(_selectedfile):
    noimagestxt = ["There are no images in a text file"]
    global _imageresult
    _imageresult = noimagestxt


    #def kwictxt(_selectedfile):            #CAN'T FIND LIBRARY FOR THIS


def audiotxt(_selectedfile):
    noaudiotxt = ["There is audio in a text file"]
    global _audioresult
    _audioresult = noaudiotxt


def videotxt(_selectedfile):
    novideotxt = ["There is no video in a text file"]
    global _videoresult
    _videoresult = novideotxt




