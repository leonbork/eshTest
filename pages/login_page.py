from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://web.eos.bnk-il.com/auth"

    USERNAME_INPUT = (By.XPATH, "//div[@data-testid='input']//input[@type='text']")  # Replace with actual locator
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Password']")  # Replace with actual locator
    LOGIN_BUTTON = (By.XPATH, "//button[.//span[text()='Login']]")       # Replace with actual locator

    def open(self):
        self.open_url(self.URL)

    def login(self, username, password):
        self.wait_for_element(self.USERNAME_INPUT).send_keys(username)
        self.wait_for_element(self.PASSWORD_INPUT).send_keys(password)
        self.wait_for_element(self.LOGIN_BUTTON).click()
