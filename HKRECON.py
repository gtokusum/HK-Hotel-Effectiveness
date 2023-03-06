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

# init global variables for when points == NAN 
kings = ['GK','AGK','B5GK','DGK','STK']
queens = ['GQQ','GTT','STB','DCGQQ','ASJQQ']
suitesK = ['SGK','STE1']
SuitesS = 'STE2'
suitesQ = ['SGQQ','ASGQQ']
headerRow = ['B1','C1','D1','E1']
headerValues = ['King Checkout','King Stayover','Queen Checkout','Queen Stayover']

# pull data from boards. outputs dataframe of excel file
def pull(name):
    return pd.read_excel(name)


# clean dataframe. returns dictionary with name as key and dataframe as value
def clean(df):
    output = df[['Room Type','Employee Assigned','Room Points','Service Type','Action']]
    output.sort_values(by='Employee Assigned')
    return dict(tuple(output.groupby(by='Employee Assigned')))


# calculates workload by employee 
def process(dict):
    finCount = []
    for i in dict:
        finCount.append(i.key,counter(i.value))
    return finCount
        

# returns count per employee
def counter(data):
    count = initDict()
    for i in range(len(data['Room Points'])):
        points = data['Room Points'].iloc[i]
        if pd.isna(points) == True:
            # write code to check service type and room
            room = data['Room Type'].iloc[i]
            service = data['Service Type'].iloc[i]
            if service == 'Check-Out':
                if room in kings:
                    count['King Checkout'] = count['King Checkout'] + 1
                elif room in queens:
                    count['Queen Checkout'] = count['Queen Checkout'] + 1
                # figure out what the suites will be coded as and add code as necessary
                elif room in suitesK:
                    pass
                elif room in suitesQ:
                    pass
                else:
                    pass
            else:
                if room in kings:
                    count['King Stayover'] = count['King Stayover'] + 1
                elif room in queens:
                    count['Queen Stayover'] = count['Queen Checkout'] + 1
                # figure out what the suites will be coded as and add code as necessary
                elif room in suitesK:
                    pass
                elif room in suitesQ:
                    pass
                else:
                    pass
        else:
            match points:
                case 3:
                    count['King Stayover'] = count['King Stayover'] + 1
                case 4:
                    count['Queen Stayover'] = count['Queen Stayover'] + 1
                case 6:
                    count['King Checkout'] = count["King Checkout"] + 1 
                case 7:
                    count['Queen Checkout'] = count['Queen Checkout'] + 1
                # figure out what the suites will be coded as and add code as necessary
                case 8:
                    pass
                case 9:
                    pass
                case 10:
                    pass
                case 12:
                    pass
                case _:
                    pass
    
    return count

# initializes Dictionary for room count
def initDict():
    # change according to new set up 
    return {'King Checkout':0,'King Stayover':0,'Queen Checkout':0,'Queen Stayover':0}

# creates workbook
def create():
    return pxl.Workbook()

# initilize excel sheet for headers
def initExcel(wb):
    headers = initDict()
    sheet = wb.active
    for i in range(len(headers)):
        sheet[headerRow[i]].value = headerValues[i]
    return wb



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