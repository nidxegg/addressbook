from selenium.webdriver.common.by import By
from model.group import Group
class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        # open groups page
        if not (self.app.driver.current_url.endswith("/group.php") and len(self.app.driver.find_elements(By.NAME, "new")) > 0):
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
        self.group_cache = None

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
        self.del_groups_by_index(0)


    def select_first_group(self):
        driver = self.app.driver
        driver.find_element(By.NAME, "selected[]").click()

    def modify_first_group(self):
        # open groups page
        self.modify_group_by_index(0)

    def count(self):
        driver = self.app.driver
        self.open_groups_page()
        return len(driver.find_elements(By.NAME, "selected[]"))

    group_cache = None


    def get_group_list(self):
        if self.group_cache is None:
            driver = self.app.driver
            self.open_groups_page()
            self.group_cache = []
            for element in driver.find_elements(By.CSS_SELECTOR, "span.group"):
                text = element.text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.group_cache.append(Group(groupname=text, id=id))
        return list(self.group_cache)


    def del_groups_by_index(self, index):
        driver = self.app.driver
        self.open_groups_page()
        self.select_group_by_index(index)
        driver.find_element(By.NAME, "delete").click()
        self.open_groups_page()
        self.group_cache = None

    def select_group_by_index(self, index):
        driver = self.app.driver
        driver.find_elements(By.NAME, "selected[]")[index].click()

    def modify_group_by_index(self, index, new_group_data):
        # open groups page
        driver = self.app.driver
        self.open_groups_page()
        self.select_group_by_index(index)
        driver.find_element(By.NAME, "edit").click()
        self.fill_group_form(new_group_data)
        driver.find_element(By.NAME, "update").click()
        self.group_cache = None



