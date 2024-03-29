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
from tkinter import ttk
import pandas as pd
from HKRECONCHA import main

WIDTH = 200
LENGTH = 100

# Global variables for easier typing 
suitec,suites,kings,kingc,queens,queenc = 'Suite Checkout','Suite Stayover','King Stayover','King Checkout','Queen Stayover','Queen Checkout'


# file browser function
def fileBrowse():
    filename = filedialog.askopenfilename(initialdir = '/Downloads',title='Select a File', filetypes=[("Excel files","*.xlsx")])
    
    
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

# converts dataframe rows to list of tuples
def dfValues(df):
    # print(df)
    xlst = []
    ind = [i for i in df.index]
    for i in range(len(df)):
        tmpLst = df.iloc[i,:].values.flatten().tolist()
        tmpLst.insert(0,ind[i])
        xlst.append(tuple(tmpLst))
    return xlst

# display dataframe as a pop up window 
def displayData(df):
    root = tk.Tk()
    # change later
    root.title('Hotel Effectiveness Report')
    root.resizable(width=800,height=400)
    columns = ('HK Name',suites,suitec,'King Stayover','King Checkout','Queen Stayover','Queen Checkout')
    values = dfValues(df)
    tree = ttk.Treeview(root,columns = columns,show='headings')
    tree.heading('HK Name',text='HK Name')
    tree.column('HK Name',minwidth=0,width=150,stretch=False)
    tree.heading(kings,text = 'King Stayover')
    tree.column(kings,minwidth=0,width=150,stretch=False)
    tree.heading(kingc, text = 'King Checkout')
    tree.column(kingc,minwidth=0,width=150,stretch=False)
    tree.heading(queens,text = 'Queen Stayover')
    tree.column(queens,minwidth=0,width=150,stretch=False)
    tree.heading(queenc,text = 'Queen Checkout')
    tree.column(queenc,minwidth=0,width=150,stretch=False)
    tree.heading(suites,text = 'Suite Stayover')
    tree.column(suites,minwidth=0,width=150,stretch=False)
    tree.heading(suitec,text = 'Suite Checkout')
    tree.column(suitec,minwidth=0,width=150,stretch=False)
    for i in range(len(values)):
        if i%2 == 0:
            tree.insert('',tk.END,values=values[i],tags=('evenrow',))
        else:
            tree.insert('',tk.END,values=values[i],tags=('oddrow',))
            # change color of odd rows here. Go to http://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html to see all the colors available
    tree.tag_configure('oddrow',background='light sky blue')
    tree.grid(row=0,column=0,sticky='nsew')
    root.mainloop()


# builds and run gui
root = tk.Tk()
root.geometry(f"{WIDTH}x{LENGTH}")
root.title("Hotel Effectiveness Room Clean Reporter")
filebnt = tk.Button(root,text='Select File and Start',command=fileBrowse)
filebnt.pack()
root.mainloop()