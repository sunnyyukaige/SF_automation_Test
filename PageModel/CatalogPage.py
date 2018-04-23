__author__ = 'sunny.yu2'
from PageModel.BasePage import BasePage
from selenium.webdriver.common.by import By
import time


class CatalogPage(BasePage):
    # PageObject Definition

    config = (By.CSS_SELECTOR, 'div.listing-actions-area button.secondary')
    pricing = (By.CSS_SELECTOR, 'div.sidebar--configure-product button.secondary')
    validate = (By.CSS_SELECTOR, 'div.sidebar--configure-product button.primary')

    def selectPrograme(self, value):
        self.click_element((By.LINK_TEXT, value))
        self.Hard_Sleep(5)

    def gotoConfig(self, index):
        """
        Select config by index
        :param value: the index of config button
        :return:
        """
        self.Find_Elements(self.config)[index].click()

        # Go validate sale

    def goValidate(self):
        self.click_element(self.validate)
        self.Hard_Sleep(5)

        # Go pricing sale

    def goPricing(self):
        self.click_element(self.pricing)
        self.Hard_Sleep(5)

        # Go finialise sale

    def goFinialise(self):
        self.select_button('Finalize').click()
