from selenium.webdriver.common.by import By


class OrderPage:

    def __init__(self, driver):  # This constructor get the driver from the actual test case
        self.driver = driver

    view_order_history_css_locator = "#content>ul:nth-child(4)>li:nth-child(1)>a:nth-child(1)"
    order_history_header_label = "#content>h1:nth-child(1)"

    def click_order_history_link(self):
        self.driver.find_element(By.CSS_SELECTOR, self.view_order_history_css_locator).click()

    def verify_header_in_the_order_page(self):
        self.driver.find_element(By.CSS_SELECTOR, self.order_history_header_label).is_displayed()
