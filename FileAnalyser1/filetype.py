__author__ = 'cavanaghb'

from FileAnalyser1 import txtfiles

def selectedfiletype(selectedfile):   #this is the open file function linked back to the open file button

    if selectedfile.endswith('.txt'):

        newbinaryfile = open('binaryfiletext.txt', 'w+')              #create a new file to transfer the data to
        newhexfile = open('hexfiletext.txt', 'w+')

        newbinaryfile.write(selectedfile)
        newhexfile.write(selectedfile)          #transfer the data to the new files

        txtfiles.filedetailstxt(selectedfile)           #get the file details



    elif selectedfile.endswith('.bmp'):
        newbinaryfile = open("binaryfilebmp.bmp", 'w+')
        newhexfile = open("hexfilebmp.bmp", 'w+')
