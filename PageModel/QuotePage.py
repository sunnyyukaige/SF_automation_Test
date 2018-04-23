__author__ = 'sunny.yu2'
from PageModel.BasePage import BasePage
from selenium.webdriver.common.by import By
import time


class QuotePage(BasePage):
    # PageObject Definition
    button_Production = (By.CSS_SELECTOR, "img[alt='Choose Products']")
    button_Delete = (By.LINK_TEXT, 'Del')

    # Go to production page
    def gotoProduction(self):
        self.click_element(self.button_Production)
        # Select programe by value

    # Delete the frist  quote
    def deleteQuote(self):
        self.click_element(self.button_delete)
