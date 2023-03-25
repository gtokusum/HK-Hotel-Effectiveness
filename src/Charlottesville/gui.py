'''
GUI to allow easier use of HKRECON.py.
Minimal GUI with one button that opens file selector and runs HKRECON.py
Uses pop out window to display table w/names and count

Dependencies:
Tkinter
Pandas
HKRECON
'''
import tkinter as tk
from tkinter import filedialog
import pandas as pd
from HKRECONCHA import main

WIDTH = 200
LENGTH = 100

# file browser function
def fileBrowse():
    filename = filedialog.askopenfilename(initialdir = '/',title='Select a File', filetypes=[("Excel files","*.xlsx")])
    
    
    try:
        displayData(main(filename))
    except:
        displayError()
    
def displayError():
    win = tk.Toplevel(root)
    message = 'Incorrect Excel Sheet'
    tk.Label(win,text='File Error').pack()
    text = tk.Text(win)
    text.insert(tk.END,str(message))
    text.pack()



# display dataframe as a pop up window 
def displayData(df):  
    win = tk.Toplevel(root)
    # win.geometry('800x400')
    message = "Report Output"
    tk.Label(win,text=message).pack()
    text = tk.Text(win,width=105)
    text.insert(tk.END,df)
    # text.insert(tk.END, str(df))
    text.pack()


# builds and run gui
root = tk.Tk()
root.geometry(f"{WIDTH}x{LENGTH}")
root.title("Hotel Effectiveness Room Clean Reporter")
filebnt = tk.Button(root,text='Select File and Start',command=fileBrowse)
filebnt.pack()
root.mainloop()