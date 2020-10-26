from selenium.webdriver.common.by import By
class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        # open groups page
        self.app.driver.find_element(By.LINK_TEXT, "groups").click()

    def view_groups(self):
        # view group
        self.app.driver.find_element(By.LINK_TEXT, "groups").click()

    def create_groups(self, group):
        # init group creation
        driver = self.app.driver
        self.open_groups_page()
        driver.find_element(By.NAME, "new").click()
        # fill group form
        driver.find_element(By.NAME, "group_name").click()
        driver.find_element(By.NAME, "group_name").send_keys(group.groupname)
        driver.find_element(By.NAME, "group_header").click()
        driver.find_element(By.NAME, "group_header").send_keys(group.groupheader)
        driver.find_element(By.NAME, "group_footer").click()
        driver.find_element(By.NAME, "group_footer").send_keys(group.groupfooter)
        driver.find_element(By.NAME, "submit").click()
        self.open_groups_page()
