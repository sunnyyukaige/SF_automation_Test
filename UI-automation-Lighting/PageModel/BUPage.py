__author__ = 'sunny.yu2'
from PageModel.BasePage import BasePage
from selenium.webdriver.common.by import By


class BUPage(BasePage):
    # PageObject Definition
    button_go = (By.NAME, 'go')
    link_chinaFranchise = (By.LINK_TEXT, 'China Franchise')
    label_pageDescription = (By.CLASS_NAME, 'pageDescription')
    button_edit = (By.NAME, 'edit')

    # Search BU button
    def searchBU(self):
        self.click_element(self.button_go)

    # Select frist BU
    def selectBU(self):
        self.click_element(self.link_chinaFranchise)

    # Check the name of BU
    def checkBUname(self, name):
        assert self.get_text_element(self.label_pageDescription) == name

    # Click edit button
    def clickEdit(self):
        self.click_element(self.button_edit)

    # Select market name
    def selectMarketName(self, value):
        self.select_by_label('Market Name', value)

    # Select bussiness line name
    def selectBusinessLineName(self, value):
        self.select_by_label('Business Line Name', value)

    # Select business unit name
    def setBusinessUnitName(self, value):
        self.input_by_label("Business Unit Name", value)

    # Select business unit code
    def setBusinessUnitCode(self, value):
        self.input_by_label("usiness Unit Code", value)
