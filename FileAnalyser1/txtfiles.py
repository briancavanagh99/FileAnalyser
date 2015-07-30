__author__ = 'cavanaghb'


#conversion file to act as trigger for parent window file to binary


import os


def newtxtfiles(_selectedfile):

    newbinaryfile = open('binaryfiletext.txt', 'w+')              #create a new file to transfer the data to
    newhexfile = open('hexfiletext.txt', 'w+')

    newbinaryfile.write(_selectedfile)
    newhexfile.write(_selectedfile)          #transfer the data to the new files


def filedetailstxt(_selectedfile):       #preform file analysis on the original file

    #file name
    filename =  os.path.splitext(_selectedfile)
    print(filename, '\n')

    #file size
    filesize = os.stat(_selectedfile)
    print(filesize, '\n')

    #file extension
    fileextension = os.path.splitext(_selectedfile)
    print(fileextension)

    #metadata

'''
def bincontxt():
    filetype.binhexfile =

def hexcontxt():
    filetype.newhexfile =

def uritxt():
    filetype.binhexfile =
    filetype.newhexfile =


def imagestxt():


def audiotxt():


def videotxt():
'''




