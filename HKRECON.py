import pandas as pd
import openpyxl as pxl
import os

'''
Partially automates the Houskeeping Reconciliation sheet for the night audit process in Hotel Effectiveness
Will pull through the boards downloaded from Infor HMS and create a new excel file with names and workload

Dependencies:
Pandas - creates tables from excel to support with data processing
Openpyxl - excel support
'''
kings = ['GK','AGK','B5GK','DGK','STK']
queens = ['GQQ','GTT','STB','DCGQQ','ASJQQ']
suitesK = ['SGK','STE1']
SuitesS = 'STE2'
suitesQ = ['SGQQ','ASGQQ']


# pull data from boards
def pull(name):
    return pd.read_excel(name)


# clean dataframe 
def clean(df):
    output = df[['Room Type','Employee Assigned','Room Points','Service Type','Action']]
    output.sort_values(by='Employee Assigned')
    return dict(tuple(output.groupby(by='Employee Assigned')))


# calculates workload by employee 
def process(dict):
    finCount = []
    for i in dict:
        finCount.append(counter(i))
        

# returns count per employee
def counter(dict):
    count = initDict()


# initializes Dictionary for room count
def initDict():
    # change according to new set up 
    return {'King Checkout':0,'King Stayover':0,'Queen Checkout':0,'Queen Stayover':0}

# creates workbook
def create():
    return pxl.Workbook()

# saves calculations in excel format
def save(pxlobj):
    pxlobj.save("HE REPORT.xlsx")

# takes in list and adds each item to spreadsheet
def fill(lst):
    pass


# Driver for program
def main():
    pass


if __name__ == '__main__':
    main()