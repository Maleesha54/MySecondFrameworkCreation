import time

from PageObject.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from PageObject.OrderPage import OrderPage


class TestMyOrders:
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()

    def test_view_my_order(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.input_email_into_the_email_field(self.email)
        self.lp.input_password_into_the_password_field(self.password)
        self.lp.click_on_the_login_button()
        self.lp.verify_my_account_text()

        self.order_pge = OrderPage(self.driver)
        self.order_pge.click_order_history_link()
        self.order_pge.verify_header_in_the_order_page()
