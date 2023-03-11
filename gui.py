'''
GUI to allow easier use of HKRECON.py.
Will include pop out file selector 

Dependencies:
Tkinter
HKRECON
'''
import tkinter as tk
from tkinter import filedialog
from HKRECON import main

WIDTH = 200
LENGTH = 100

# file browser function 
def fileBrowse():
    filename = filedialog.askopenfilename(initialdir = '/',
                                          title = 'select a file',)
    main(filename)
    
    # label_file_explorer.configure(text='File Opened: '+filename)

# display dataframe after being saved to excel file
def displayData():
    pass


# builds and displays gui
root = tk.Tk()
root.geometry(f"{WIDTH}x{LENGTH}")
root.title("Hotel Effectiveness Room Clean Reporter")
filebnt = tk.Button(root,text='Select File and Start',command=fileBrowse)
filebnt.pack()
root.mainloop()