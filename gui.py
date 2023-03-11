'''
GUI to allow easier use of HKRECON.py.
Will include pop out file selector 

Dependencies:
Tkinter
HKRECON
'''
import tkinter as tk
from tkinter import filedialog
import pandas as pd
from HKRECON import main

WIDTH = 200
LENGTH = 100

# file browser function 
def fileBrowse():
    filename = filedialog.askopenfilename(initialdir = '/',
                                          title = 'select a file',)
    main(filename)
    displayData()
    # label_file_explorer.configure(text='File Opened: '+filename)

# display dataframe after being saved to excel file
def displayData():  
    df = pd.read_excel("HERECON.xlsx")
    win = tk.Toplevel()
    message = "Report Output"
    tk.Label(win,text=message).pack()
    text = tk.Text(win)
    text.insert(tk.END, str(df))
    text.pack()

# builds and displays gui
root = tk.Tk()
root.geometry(f"{WIDTH}x{LENGTH}")
root.title("Hotel Effectiveness Room Clean Reporter")
filebnt = tk.Button(root,text='Select File and Start',command=fileBrowse)
filebnt.pack()
root.mainloop()