__author__ = 'cavanaghb'

#file for parent window that all other windows will become a child of

import tkinter
from tkinter import filedialog
from FileAnalyser1 import filetype
import tkinter.ttk as ttk
from FileAnalyser1 import txtfiles
import tkinter.scrolledtext
import cv2

class MainWindow(tkinter.Frame):
    
    WINDOW_WIDTH = 1000
    WINDOW_HEIGHT = 600
    TAB_WIDTH = WINDOW_WIDTH - 15
    TAB_HEIGHT = WINDOW_HEIGHT - 50
    
    file_details_tab = None
    txt_tab = None
    bin_tab = None
    hex_tab = None
    img_tab = None
    uri_tab = None
    csv_tab = None
    aud_tab = None
    vid_tab = None

    def __init__(self, root):             #first window dialog to open

        tkinter.Frame.__init__(self, root)

        filebutton = tkinter.Button(root, text="Open File for Selection button", width=35, command=self.getfile)
        filebutton.pack()

        quitbutton = tkinter.Button(root, text="Quit", width=10, command=quit)
        quitbutton.pack()
        
        #print("Window => %sx%s" % (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        #print("Tabs => %sx%s" % (self.TAB_WIDTH, self.TAB_HEIGHT))


    def destroy_visible_tabs(self):
        if self.file_details_tab:
            self.file_details_tab.destroy()
            
        if self.txt_tab:
            self.txt_tab.destroy()
            
        if self.bin_tab:
            self.bin_tab.destroy()
        
        if self.hex_tab:
            self.hex_tab.destroy()
            
        if self.uri_tab:
            self.uri_tab.destroy()
            
        if self.img_tab:
            self.img_tab.destroy()
            
        if self.csv_tab:
            self.csv_tab.destroy()
            
        if self.aud_tab:
            self.aud_tab.destroy()
            
        if self.vid_tab:
            self.vid_tab.destroy()
    
    
    def show_file_details(self, file_details):
        self.file_details_tab = ttk.Frame(newnotebook, width=self.TAB_WIDTH, height=self.TAB_HEIGHT)
        results = ttk.Label(self.file_details_tab, text=file_details)
        results.pack()
        newnotebook.add(self.file_details_tab, text="File Details")  
    
    
    def show_txt_result(self, txt_result):
        self.txt_tab = ttk.Frame(newnotebook, width=self.TAB_WIDTH, height=self.TAB_HEIGHT)
        results = ttk.Label(self.txt_tab, text=txt_result)
        results.pack()
        newscrollbar = tkinter.Scrollbar(self.txt_tab)
        newscrollbar.pack(side='right', fill='y')
        newnotebook.add(self.txt_tab, text="Text")
    
    
    def show_bin_result(self, bin_result):
        self.bin_tab = ttk.Frame(newnotebook, width=self.TAB_WIDTH, height=self.TAB_HEIGHT)
        newscrollbar = tkinter.Scrollbar(self.bin_tab)
        newscrollbar.pack(side='right', fill='y')

        results = tkinter.Text(self.bin_tab, wrap='word')
        results.insert("end", bin_result)
        results.pack()

        results.config(yscrollcommand=newscrollbar.set)
        newscrollbar.config(command=results.yview)
        newnotebook.add(self.bin_tab, text="Raw Binary")
    
    
    def show_hex_result(self, hex_result):
        self.hex_tab = ttk.Frame(newnotebook, width=self.TAB_WIDTH, height=self.TAB_HEIGHT)
        newscrollbar = tkinter.Scrollbar(self.hex_tab)
        newscrollbar.pack(side='right', fill='y')

        results = tkinter.Text(self.hex_tab, wrap='word')
        results.insert("end", hex_result)
        results.pack()

        results.config(yscrollcommand=newscrollbar.set)
        newscrollbar.config(command=results.yview) 
        newnotebook.add(self.hex_tab, text="Raw Hex")
        
    def show_uri_result(self,uri_result):
        self.uri_tab = ttk.Frame(newnotebook, width=self.TAB_WIDTH, height=self.TAB_HEIGHT)
        results = ttk.Label(self.uri_tab, text=uri_result)
        results.pack()
        newscrollbar = tkinter.Scrollbar(self.uri_tab)
        newscrollbar.pack(side='right', fill='y')
        newnotebook.add(self.uri_tab, text="URI")
    
    
    def show_img_result(self, img_result):
        self.img_tab = ttk.Frame(newnotebook, width=self.TAB_WIDTH, height=self.TAB_HEIGHT)
        results = ttk.Label(self.img_tab, text=img_result)
        results.pack()
        newnotebook.add(self.img_tab, text="Images")
    
    
    def show_aud_result(self, aud_result):
        self.aud_tab = ttk.Frame(newnotebook, width=self.TAB_WIDTH, height=self.TAB_HEIGHT)
        results = ttk.Label(self.aud_tab, text=aud_result)
        results.pack()
        newnotebook.add(self.aud_tab, text="Audio")
    
    
    def show_vid_result(self, vid_result):
        self.vid_tab = ttk.Frame(newnotebook, width=self.TAB_WIDTH, height=self.TAB_HEIGHT)
        button = tkinter.Button(self.vid_tab, text="Play Video", width=15, command = lambda:self.play_video(vid_result))
        button.pack()
        newnotebook.add(self.vid_tab, text="Video")
    
    
    def show_csv_result(self, csv_result):
        self.csv_tab = ttk.Frame(newnotebook, width=self.TAB_WIDTH, height=self.TAB_HEIGHT)
        results = ttk.Label(self.csv_tab, text=csv_result)
        results.pack()
        newnotebook.add(self.csv_tab, text="CSV")
    
    
    def play_video(self, filepath):
        cap = cv2.VideoCapture(filepath)
        
        while (cap.isOpened()):
            ret, frame = cap.read()
            cv2.imshow(filepath, frame)
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()
        

    def getfile(self):   #this is the open file function linked back to the open file button
        selected_file = filedialog.askopenfilename(filetypes=[('All files', '*.*')])   #select and open a file
        file_result = filetype.analyse_file(selected_file)  # execute the filetype function to confirm file type and start conversion

        self.destroy_visible_tabs()
        
        if not file_result.file_details:
            self.show_file_details("\nThe file type of [%s] is unsupported.\n\nPlease select one of txt, jpg, jpeg, csv or avi\n\n" % selected_file)
            newnotebook.pack()
            return
        
        self.show_file_details(file_result.file_details)
        
        if file_result.txt_result:
            self.show_txt_result(file_result.txt_result)
            
        if file_result.bin_result:
            self.show_bin_result(file_result.bin_result)
            
        if file_result.hex_result:
            self.show_hex_result(file_result.hex_result)
            
        if file_result.uri_result:
            self.show_uri_result(file_result.uri_result)
            
        if file_result.img_result:
            self.show_img_result(file_result.img_result)
            
        if file_result.csv_result:
            self.show_csv_result(file_result.csv_result)
        
        if file_result.aud_result:
            self.show_aud_result(file_result.aud_result)
            
        if file_result.vid_result:
            self.show_vid_result(file_result.vid_result)
            
        newnotebook.pack()


if __name__=='__main__': # run the main instance to start the program
    root = tkinter.Tk()
    newnotebook = ttk.Notebook(root)
    MainWindow(root).pack()
    root.geometry("%sx%s+200+50" % (MainWindow.WINDOW_WIDTH, MainWindow.WINDOW_HEIGHT))
    root.title('File Analysis Tool')

    root.mainloop()
    
    
    