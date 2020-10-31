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
        self.fill_group_form(group)
        driver.find_element(By.NAME, "submit").click()
        self.open_groups_page()

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.groupname)
        self.change_field_value("group_header", group.groupheader)
        self.change_field_value("group_footer", group.groupfooter)

    def change_field_value(self, fieldname, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element(By.NAME, fieldname).click()
            driver.find_element(By.NAME, fieldname).clear()
            driver.find_element(By.NAME, fieldname).send_keys(text)

    def del_groups(self):
        driver = self.app.driver
        self.open_groups_page()
        self.select_first_group()
        driver.find_element(By.NAME, "delete").click()
        self.open_groups_page()

    def select_first_group(self):
        driver = self.app.driver
        driver.find_element(By.NAME, "selected[]").click()

    def modify_first_group(self, new_group_data):
        # open groups page
        driver = self.app.driver
        self.app.driver.find_element(By.LINK_TEXT, "groups").click()
        self.open_groups_page()
        self.select_first_group()
        #open modify group page
        driver.find_element(By.NAME, "edit").click()
        self.fill_group_form(new_group_data)

        driver.find_element(By.NAME, "update").click()





