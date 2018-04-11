__author__ = 'sunny.yu2'
from PageModel.BasePage import BasePage
from selenium.webdriver.common.by import By


class ContenMapPage(BasePage):
    # PageObject Definition
    button_New = (By.CSS_SELECTOR, "div[title='New']")
    link_ChinaFranchise = (By.LINK_TEXT, 'China Franchise')
    label_pageDescription = (By.CLASS_NAME, 'pageDescription')
    button_edit = (By.NAME, 'edit')

    def addNew(self):
        self.Find_Element_And_Click(self.button_New)
        self.ClosethiswindowButtonExist()

    def inputContentName(self, value):
        self.InputByLabelLighting('Content Name', value)

    def selectContentMapVersion(self,value):
        self.SelectByLabelLighting('Content Map Version',value )
