__author__ = 'brian_000'

__author__ = 'cavanaghb'


#conversion file to act as trigger for parent window file to binary


import os
import re
#import binascii


def get_file_details(selectedfile):       #preform file analysis on the original file
    filename = os.path.basename(selectedfile)          #file name
    filesize = os.path.getsize(selectedfile)               #file size
    fileextension = ["This is a csv file"]         #file extension 
    
    # create a string out of each piece of data and return to the main window
    return "Filename: %s\nSize: %s bytes\nType: %s" % (str(filename), str(filesize), str(fileextension))


def get_txt(selectedfile):
    with open (selectedfile, "r") as the_file:
        txt_content = the_file.read()
    
    return txt_content


def get_bin(selectedfile):
    with open (selectedfile, "r") as the_file:
        txt_content = the_file.read()
    
    binary = ' '.join(format(ord(x), 'b') for x in txt_content)
    return binary


def get_hex(selectedfile):
    with open (selectedfile, "r") as the_file:
        file_content = the_file.read()
    
    hex_result = ' '.join(hex(ord(n)) for n in file_content)
    return hex_result


def get_uri(selectedfile):
    URIs = []
    with open(selectedfile, 'r') as f:
        for line in f:
            URIs.extend( re.findall('(http[s]?:\/\/\S+|www\.\S+|ftp:\/\/\.\S+|file:\/\/)', line, re.IGNORECASE | re.MULTILINE) )
        
    if URIs:
        return "\n".join(URIs)
    else:
        return None





