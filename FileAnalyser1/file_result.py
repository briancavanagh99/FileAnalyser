__author__ = 'cavanaghb'

class FileResult:
    
    file_details = None
    txt_result = None
    bin_result = None
    hex_result = None
    uri_result = None
    csv_result = None
    img_result = None
    aud_result = None
    vid_result = None
    
    def __init__(self, details=None, txt_res=None, bin_res=None, 
                 hex_res=None, uri_res=None, csv_res=None, 
                 img_res=None, aud_res=None, vid_res=None):
        
        self.file_details = details
        self.txt_result = txt_res
        self.bin_result = bin_res
        self.hex_result = hex_res
        self.uri_result = uri_res
        self.csv_result = csv_res
        self.img_result = img_res
        self.aud_result = aud_res
        self.vid_result = vid_res

