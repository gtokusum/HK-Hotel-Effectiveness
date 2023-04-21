# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestOpengameday():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_opengameday(self):
    self.driver.get("https://my.hoteleffectiveness.com/signin")
    self.driver.set_window_size(945, 1020)
    self.driver.find_element(By.ID, "myheqa-loginForm-field-username").send_keys("gtokusumi")
    self.driver.find_element(By.ID, "myheqa-loginForm-field-password").send_keys("password")
    self.driver.find_element(By.ID, "myheqa-loginForm-button-submit").click()
    self.driver.find_element(By.LINK_TEXT, "Start Housekeeping Gameday").click()
    self.driver.switch_to.frame(1)
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > td > label").click()
    self.driver.find_element(By.ID, "ctl00_main_btnGameDaySchedule").click()
    self.driver.switch_to.default_content()
    self.driver.switch_to.frame(1)
    self.driver.find_element(By.ID, "ctl00_main_hLinkSaveContinue").click()
    self.driver.switch_to.default_content()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-username").click()
    self.driver.find_element(By.CSS_SELECTOR, "#myheqa-navbar-dropdown-element-btnSignout > .dropdown-item").click()
