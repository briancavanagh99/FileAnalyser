__author__ = 'cavanaghb'


#USE THIS FILE TO PASS RESULTS FROM FILE TYPES TO THE FRAMES IN PARENT WINDOW


#RESULTS ARE PASSED BACK HERE AND THEN TO THE PARENT WINDOW FRAME

def resultspassing(_selectedfile):   #this is the open file function linked back to the open file button

    if _selectedfile.endswith('.txt'):