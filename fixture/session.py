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
        self.app.driver.find_element(By.LINK_TEXT, "Logout").click()