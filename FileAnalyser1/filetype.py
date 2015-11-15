__author__ = 'cavanaghb'

from FileAnalyser1 import txtfiles
from FileAnalyser1 import odtfiles
from FileAnalyser1 import jpegfiles
from FileAnalyser1 import avifiles
from FileAnalyser1 import csvfiles
from FileAnalyser1.file_result import FileResult
import re

def analyse_file(selected_filename):   #this is the open file function linked back to the open file button
    
    file_details = None
    txt_result = None
    bin_result = None
    hex_result = None
    uri_result = None
    img_result = None
    aud_result = None
    vid_result = None
    
    #
    # Only assign the above variables values if they're applicable to the selected file type
    # If they're not relevant, then they keep their default value of None, which will mean that
    # the window logic will not create a tab for that type of data
    #
    if selected_filename.endswith('.txt'):
        #txtfiles.newtxtfiles(selected_filename)          # create copies of the files
        file_details = txtfiles.get_file_details(selected_filename)  # get the file details
        txt_result = txtfiles.get_txt(selected_filename)  # get the file contents
        bin_result = txtfiles.get_bin(selected_filename)  # convert to binary
        hex_result = txtfiles.get_hex(selected_filename)  # convert to hex
        uri_result = txtfiles.get_uri(selected_filename)  # retrieve URI's

    elif re.match('^.*\.(odt|doc)$', selected_filename, re.IGNORECASE):
        #docfiles.newdocfiles(selected_filename)          # create copies of the files
        file_details = odtfiles.get_file_details(selected_filename)
        txt_result = odtfiles.get_txt(selected_filename)  
        bin_result = odtfiles.get_bin(selected_filename)  
        hex_result = odtfiles.get_hex(selected_filename)  
        uri_result = odtfiles.get_uri(selected_filename)  
        img_result = odtfiles.get_img(selected_filename)  

    elif re.match('^.*\.(avi|mp4|mpeg|mkv)$', selected_filename, re.IGNORECASE):
        #docfiles.newdocfiles(selected_filename)             #create copies of the files
        file_details = avifiles.get_file_details(selected_filename)
        bin_result = avifiles.get_bin(selected_filename)  
        hex_result = avifiles.get_hex(selected_filename)  
        aud_result = avifiles.get_aud(selected_filename)  
        vid_result = avifiles.get_vid(selected_filename)  

    elif selected_filename.endswith('.csv'):
        #docfiles.newdocfiles(selected_filename)             #create copies of the files
        file_details = csvfiles.get_file_details(selected_filename)
        txt_result = csvfiles.get_txt(selected_filename)  
        bin_result = csvfiles.get_bin(selected_filename)  
        hex_result = csvfiles.get_hex(selected_filename)  
        uri_result = csvfiles.get_uri(selected_filename)  

    elif re.match('^.*\.(jpeg|jpg|gif|png)$', selected_filename, re.IGNORECASE):
        #docfiles.newdocfiles(selected_filename)             #create copies of the files
        file_details = jpegfiles.get_file_details(selected_filename)
        bin_result = jpegfiles.get_bin(selected_filename)  
        hex_result = jpegfiles.get_hex(selected_filename)  
        img_result = jpegfiles.get_img(selected_filename)  
        
    return FileResult(details=file_details,
                      txt_res=txt_result,
                      bin_res=bin_result,
                      hex_res=hex_result,
                      uri_res=uri_result,
                      img_res=img_result,
                      aud_res=aud_result,
                      vid_res=vid_result)

