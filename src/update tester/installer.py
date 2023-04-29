'''
This file should allow for easier updating as you can download .py files and adjust if needed and create executable locally instead of downloading.
Will just need to convert this file into an executable. Should be able to regularly update after downloading updated .py files from github.
'''



import PyInstaller
import os


# checks for file containing room type/credit data. 
def checkRoomFile():
    # NOT IMPLEMENTED
    pass

# creates room file if not found. Will get data for room credit and what room types S/O & C/O equal that credit type
# Note for me: maybe use the excel sheet to grab data during script to be a universal. (might need to standardize suite values? Could cause the script to take a littl bit longer)
#                                                                                      (Especially for bigger hotels with more rooms.)
def createRoomFile():
    # NOT IMPLEMENTED
    pass

# use pyintaller to create executable. Should make it easier to allow for updates later on
def createExe(path):

    try:
        PyInstaller.__main__.run([
            path,
            '--noconfirm',
            '--onefile',
            '--windowed'
        ])
    except:
        return("An Error has occured. Please contact your System Admin")

# move executable file from C:/user/username/output to C:/user/Desktop for easier access. 
def moveFile():
    pass