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

WIDTH = 800
LENGTH = 600

# file browser function 
def fileBrowse():
    filename = filedialog.askopenfilename(initialdir = '/',
                                          title = 'select a file',)
    
    # label_file_explorer.configure(text='File Opened: '+filename)



# builds and displays gui
root = tk.Tk()
root.geometry(f"{WIDTH}x{LENGTH}")
root.title("Hotel Effectiveness Room Clean Reporter")
button = tk.Button(root,text='BUTTON',command=main)
button.pack(padx=100,pady=200)
# filebnt = tk.Button(root,text='Select File',command=fileBrowse())
# filebnt.pack(padx=10,pady=100)
root.mainloop()