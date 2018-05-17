__author__ = 'sunny.yu2'
from PageModel.BasePage import BasePage
from selenium.webdriver.common.by import By


class ContenMapPage(BasePage):
    # PageObject Definition
    button_New = (By.CSS_SELECTOR, "div[title='New']")
    link_ChinaFranchise = (By.LINK_TEXT, 'China Franchise')
    label_pageDescription = (By.CLASS_NAME, 'pageDescription')
    button_edit = (By.NAME, 'edit')

    # Add new button
    def addNew(self):
        self.click_element(self.button_New)
        self.close_this_window_button_exist()

    # Content map name by value
    def inputContentName(self, value):
        self.input_by_label_lighting('Content Name', value,True)

    # Select content map version by value
    def selectContentMapVersion(self, value):
        self.select_by_label_lighting('Content Map Version', value)
