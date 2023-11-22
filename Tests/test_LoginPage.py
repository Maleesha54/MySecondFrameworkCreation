import pytest
from PageObject.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities import excelUtilities


class TestLogin:
    baseURL = ReadConfig.getApplicationURL()
    # email = ReadConfig.getEmail()
    # password = ReadConfig.getPassword()

    @pytest.mark.parametrize("email,password", excelUtilities.get_data("TestData/testdata.xlsx", "logintestsheet"))
    def test_valid_credentials(self, setup, email, password):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.input_email_into_the_email_field(email)
        self.lp.input_password_into_the_password_field(password)
        self.lp.click_on_the_login_button()
        self.lp.verify_my_account_text()
