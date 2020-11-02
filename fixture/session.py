from selenium.webdriver.common.by import By
class SessionHelper:
    def __init__(self, app):
        self.app = app


    def login(self, user, password):
        # login
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element(By.NAME, "user").send_keys(user)
        driver.find_element(By.NAME, "pass").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def logout(self):
        # logout
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "Logout").click()

    def insue_logout(self):
        driver = self.app.driver
        if self.is_logged_in():
            self.logout()

    def is_logged_as(self, username):
        driver = self.app.driver
        return driver.find_element(By.XPATH, "//div/div[1]/form/b").text == "("+username+")"

    def is_logged_in(self):
        driver = self.app.driver
        return len(driver.find_elements(By.LINK_TEXT, "Logout")) > 0

    def ensure_login(self, username, password):
        driver = self.app.driver
        if self.is_logged_in():
            if self.is_logged_as(username):
                return
            else:
                self.logout()
        self.login(username,password)

