import pandas as pd
import openpyxl as pxl
import os

'''
Partially automates the Houskeeping Reconciliation sheet for the night audit process in Hotel Effectiveness
Will pull through the boards downloaded from Infor HMS and create a new excel file with names and workload

Dependencies:
Pandas - creates tables from excel to support with data processing
Openpyxl 
'''



# pull data from boards
def pull(name):
    return pd.read_excel(name)


# clean dataframe 
def clean(df):
    output = df[['Room Type','Employee Assigned','Room Points','Service Type','Action']]
    return output.sort_values(by='Employee Assigned')


# calculates workload by employee 
def process(df):
    pass

# returns count per employee
def counter(df):
    pass

# creates workbook
def create():
    return pxl.Workbook()

# saves calculations in excel format
def save(df):
    pass

# Driver for program
def main():
    pass


if __name__ == '__main__':
    pass