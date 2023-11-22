from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def click_element(self, by, value):
        self.find_element(by, value).click()

    def send_keys_to_element(self, by, value, keys):
        self.find_element(by, value).send_keys(keys)

    def wait_for_element_visibility(self, by, value):
        return self.wait.until(EC.visibility_of_element_located((by, value)))
