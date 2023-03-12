import pandas as pd
import openpyxl as pxl
from openpyxl.utils.dataframe import dataframe_to_rows
import os
'''
Partially automates the Houskeeping Reconciliation sheet for the night audit process in Hotel Effectiveness
Will pull through the boards downloaded from Infor HMS and create a new excel file with names and workload

Dependencies:
Pandas - creates tables from excel to support with data processing
Openpyxl - excel support (not implemented)
'''

# init global variables for when points == NAN, Likely happens when pulling boards with completed rooms
kings = ['GK','AGK','B5GK','DGK','STK']
queens = ['GQQ','GTT','STB','DCGQQ','ASJQQ']
suitesK = ['SGK','STE1']
SuitesS = 'STE2'
suitesQ = ['SGQQ','ASGQQ']
# headerRow = ['B1','C1','D1','E1']
# headerValues = ['King Checkout','King Stayover','Queen Checkout','Queen Stayover']
headerValues = ['King Stayover','King Checkout','Queen Stayover','Queen Checkout']


# pull data from boards. outputs dataframe of excel file
def pull(name):
    return pd.read_excel(name)


# clean dataframe. returns dictionaries with dataframe and names of employees
def clean(df):
    output = df[['Room Type','Employee Assigned','Room Points','Service Type','Action']]
    output.sort_values(by='Employee Assigned')
    cleaned = dict(tuple(output.groupby(by='Employee Assigned')))
    return cleaned #, [i for i in cleaned] uncomment if needed to get names. Should not need

# calculates workload by employee 
def process(dict):
    finCount = []
    for i in dict:
        # finCount.append(i.key,counter(i.value))
        finCount.append((i,counter(dict[i])))
    # print(finCount)
    return df_to_excel(finCount)
    # return True

# takes list from process() and converts to dataframe
def df_to_excel(finCount):
    names = [i[0] for i in finCount]
    # print(names)
    df = pd.DataFrame(index = names,columns=headerValues)
    for i in range(len(finCount)):
        for j in range(len(headerValues)):
            
            df.iloc[i].loc[headerValues[j]] = finCount[i][1][headerValues[j]]

    # uncomment code below if you would like to save the report as an excel file. Will send file to PATH.
    # save(df)
    return df

# returns room count by room typer per employee
# WILL NEED TO CHANGE FOR SUITESK,SUITESQ,SUITESS
def counter(data):
    count = initDict()
    for i in range(len(data['Room Points'])):
        points = data['Room Points'].iloc[i]
        if pd.isna(points) == True:
            # check service type and room
            room = data['Room Type'].iloc[i]
            service = data['Service Type'].iloc[i]

            # change values here to adjust per property
            if service == 'Check-Out':
                if room in kings:
                    count['King Checkout'] = count['King Checkout'] + 1
                elif room in queens:
                    count['Queen Checkout'] = count['Queen Checkout'] + 1
                elif room in suitesK:
                    count['King Checkout'] = count['King Checkout'] + 1
                    count['King Stayover'] = count['King Stayover'] + 1
                elif room in suitesQ:
                    count['King Stayover'] = count['King Stayover'] + 1
                    count['Queen Checkout'] = count['Queen Checkout'] + 1 
                else:
                    count['King Checkout'] = count['King Stayover'] + 2
            else:
                if room in kings:
                    count['King Stayover'] = count['King Stayover'] + 1
                elif room in queens:
                    count['Queen Stayover'] = count['Queen Checkout'] + 1
                elif room in suitesK:
                    count['King Checkout'] = count['King Checkout'] + 1
                elif room in suitesQ:
                    count['Queen Checkout'] = count['Queen Checkout'] + 1
                else:
                    count['Queen Stayover'] = count['Queen Stayover'] + 2
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
                case 8:
                    count['Queen Stayover'] = count['Queen Stayover'] + 2
                case 9:
                    count['King Checkout'] = count['King Checkout'] + 1
                    count['King Stayover'] = count['King Stayover'] + 1
                case 10:
                    count['King Stayover'] = count['King Stayover'] + 1
                    count['Queen Checkout'] = count['Queen Checkout'] + 1
                case 12:
                    count['King Checkout'] = count['King Stayover'] + 2
                case _:
                    pass
    
    return count

# initializes Dictionary for room count
def initDict():
    # Add more if needed. i.e. more room types available on HE
    return {'King Checkout':0,'King Stayover':0,'Queen Checkout':0,'Queen Stayover':0}

# saves calculations in excel format
def save(df):
    df.to_excel("HERECON.xlsx")

# Driver for program, name needs to be file name/location
# Using gui.py will allow for selection of file. 
def main(name):
    # name = "Sheet1 (5).xlsx"
    pulledData = pull(name)
    cleaned = clean(pulledData)
    # worked = process(cleaned)
    return process(cleaned)
    # if worked:
    #     print("DONE")

# Uncomment below if running script from here instead of gui.py
# if __name__ == '__main__':
#     main()