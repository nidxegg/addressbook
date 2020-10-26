from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        # open home page
        self.driver.get("http://addressbook/")

    def destroy(self):
        self.driver.quit()