import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



def start():
    driver = webdriver.Chrome()
    return driver

def toGameday(driver):
    driver.get("https://my.hoteleffectiveness.com/signin")
    driver.set_window_size(945, 1020)
    driver.find_element(By.ID, "myheqa-loginForm-field-username").send_keys("gtokusumi") #username
    driver.find_element(By.ID, "myheqa-loginForm-field-password").send_keys("password") #password
    driver.find_element(By.ID, "myheqa-loginForm-button-submit").click() #click on log in button

    # waits until it finds link to housekeeping gameday set up page. once found click it
    WebDriverWait(driver,timeout=30).until(lambda d: d.find_element(By.XPATH,"/html/body/he-root/div/ng-component/div/main/ng-component/ng-component/he-page-body-container/div/he-hotel-view-widgets/div/div/div[1]/div/he-dynamic-component-wrapper/ng-component/div/form/div[3]/a")) #waits until start game day button
    driver.find_element(By.XPATH, "/html/body/he-root/div/ng-component/div/main/ng-component/ng-component/he-page-body-container/div/he-hotel-view-widgets/div/div/div[1]/div/he-dynamic-component-wrapper/ng-component/div/form/div[3]/a").click() #click start gameday button

    # waits for the receiver frame to be found then switches to it to click on 'Show Only Scheduled Room Attendants'
    WebDriverWait(driver,timeout=30).until(expected_conditions.frame_to_be_available_and_switch_to_it((By.ID,'receiver')))
    driver.switch_to.default_content()
    # driver.implicitly_wait(15) #uncomment if needed. 
    driver.switch_to.frame('receiver') #swtich frame to receiver 
    WebDriverWait(driver,timeout=30).until(lambda d: d.find_element(By.ID,'ctl00_main_rlHskpList')) #wait until it locates table that includes the button for only scheduled attendants
    table = driver.find_element(By.ID,'ctl00_main_rlHskpList') #find table and save as table variable
    table.find_element(By.ID, "ctl00_main_rlHskpList_1").click() #find radio button and click
    driver.find_element(By.NAME, "ctl00$main$btnGameDaySchedule").click() #go to gameday grid

    driver.switch_to.default_content() #switches back to default content


def inputValues(df,driver):
    # from random import randint
    empNum = len(df) # number of employees for the given day. Can be pulled from the dataframe
    driver.switch_to.frame('receiver') #swtich to frame with grid
    grid = driver.find_element(By.ID,'ctl00_main_tblGameDaySchedule') # finds grid and saves as variable
    newDf = df
    newDf.columns = ['2','3','4','5'] #sets dataframe columns to match with Hotel Effectiveness

    a,b = 2,6
    # will loop through each cell and input value
    for j in range(0,empNum): # row value
        for i in range(a,b): # column value
            grid.find_element(By.ID, f'ctl00_main_txtScheduleDetail1{i}0{j}').send_keys(int(newDf.iloc[j][str(i)]))

    #switch back to default content
    driver.switch_to.default_content()


def save(driver):
    driver.switch_to.frame('receiver') # swtiches back to reciever frame
    driver.find_element(By.ID,'ctl00_main_rdExportExcel').click() #finds the radio button to download an excel file of the grid, uncomment if not needed
    driver.find_element(By.ID,'ctl00_main_hLinkSaveContinue').click() # finds the save button and clicks on it.
    driver.switch_to.default_content()

from HKRECON import main

def mainFunc(df):
# def mainFunc():
    # df = main('Sheet1 (14).xlsx')
    driver = start()
    toGameday(driver)
    inputValues(df,driver)
    # save(driver)
    # driver.quit()
    quit = input('quit:')
    if int(quit) == 1:
        driver.quit()

if __name__ == '__main__':
    mainFunc()
