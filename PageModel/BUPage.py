__author__ = 'sunny.yu2'
from PageModel.BasePage import BasePage
from selenium.webdriver.common.by import By


class BUPage(BasePage):
    # PageObject Definition
    button_go = (By.NAME, 'go')
    link_ChinaFranchise = (By.LINK_TEXT, 'China Franchise')
    label_pageDescription = (By.CLASS_NAME,'pageDescription')
    button_edit=(By.NAME,'edit')

    def searchBU(self):
        self.Find_Element_And_Click(self.button_go)

    def selectBU(self):
        self.Find_Element_And_Click(self.link_ChinaFranchise)

    def checkBUname(self,name):
        assert self.Find_Element_And_Get_Text(self.label_pageDescription)==name

    def clickEdit(self):
        self.Find_Element_And_Click(self.button_edit)

    def selectMarketName(self,value):
        self.SelectByLabel('Market Name',value)

    def selectBusinessLineName(self,value):
        self.SelectByLabel('Business Line Name',value)

    def setBusinessUnitName(self,value):
        self.InputByLabel("Business Unit Name",value)

    def setBusinessUnitCode(self,value):
        self.InputByLabel("usiness Unit Code",value)



