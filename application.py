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

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def open_groups_page(self):
        # open groups page
        self.driver.find_element(By.LINK_TEXT, "groups").click()

    def login(self, user, password):
        # login
        self.open_home_page()
        self.driver.find_element(By.NAME, "user").send_keys(user)
        self.driver.find_element(By.NAME, "pass").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def open_home_page(self):
        # open home page
        self.driver.get("http://addressbook/")

    def logout(self):
        # logout
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

    def view_groups(self):
        # view group
        self.driver.find_element(By.LINK_TEXT, "groups").click()

    def create_groups(self, group):
        # init group creation
        self.open_groups_page()
        self.driver.find_element(By.NAME, "new").click()
        # fill group form
        self.driver.find_element(By.NAME, "group_name").click()
        self.driver.find_element(By.NAME, "group_name").send_keys(group.groupname)
        self.driver.find_element(By.NAME, "group_header").click()
        self.driver.find_element(By.NAME, "group_header").send_keys(group.groupheader)
        self.driver.find_element(By.NAME, "group_footer").click()
        self.driver.find_element(By.NAME, "group_footer").send_keys(group.groupfooter)
        self.driver.find_element(By.NAME, "submit").click()
        self.open_groups_page()

    def destroy(self):
        self.driver.quit()