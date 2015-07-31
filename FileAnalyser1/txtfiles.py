__author__ = 'cavanaghb'


#conversion file to act as trigger for parent window file to binary


import os
import binascii

def newtxtfiles(_selectedfile):
    newbinaryfile = open('binaryfiletext.txt', 'w+')              #create a new file to transfer the data to
    newhexfile = open('hexfiletext.txt', 'w+')

    newbinaryfile.write(_selectedfile)
    newhexfile.write(_selectedfile)          #transfer the data to the new files


def filedetailstxt(_selectedfile):       #preform file analysis on the original file

    filename = os.path.basename(_selectedfile)          #file name
    filesize = os.path.getsize(_selectedfile)               #file size
    fileextension = ["This is a text file, find out more information about '*.txt' files at", ]         #file extension

    filedetailresult = str(filename) + str(filesize) + str(fileextension)        #create a string out of each piece of data and return to the main window
    global _filedetailresult
    _filedetailresult = filedetailresult




def bincontxt(_selectedfile):

    binaryconvert = ' '.join(format(ord(x), 'b') for x in _selectedfile)   #NEED TO CONFIRM THE FULL WORKING OF THIS!!!
    global _binaryconvert
    _binaryconvert = binaryconvert



def hexcontxt(_selectedfile):
    hexconvert = " ".join(hex(ord(n)) for n in _selectedfile)
    global _hexconvert
    _hexconvert = hexconvert


'''
def uritxt():
    filetype.binhexfile =
    filetype.newhexfile =


def imagestxt():


def audiotxt():


def videotxt():
'''




