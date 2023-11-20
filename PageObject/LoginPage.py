from selenium.webdriver.common.by import By

from PageObject.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):  # This constructor get the driver from the actual test case
        # self.driver = driver    # Initiate the local driver and now the driver belong to the class then we can access the driver by using self keyword
        super().__init__(driver)

    input_email_id_locator = "input-email"
    input_password_id_locator = "input-password"
    login_button_css_selector = "input.btn"
    edit_account_link_text_locator = "#content>ul:nth-child(2)>li:nth-child(1)>a:nth-child(1)"

    def input_email_into_the_email_field(self, email):
        # self.driver.find_element(By.ID, self.input_email_id_locator).send_keys(email)
        self.send_keys_to_element(By.ID, self.input_email_id_locator, email)

    def input_password_into_the_password_field(self, password):
        # self.driver.find_element(By.ID, self.input_password_id_locator).send_keys(password)
        self.send_keys_to_element(By.ID, self.input_password_id_locator, password)

    def click_on_the_login_button(self):
        # self.driver.find_element(By.CSS_SELECTOR, self.login_button_css_selector).click()
        self.click_element(By.CSS_SELECTOR, self.login_button_css_selector)

    def verify_my_account_text(self):
        # return self.driver.find_element(By.CSS_SELECTOR, self.edit_account_link_text_locator).is_displayed()
        return self.wait_for_element_visibility(By.CSS_SELECTOR, self.edit_account_link_text_locator).is_displayed()
