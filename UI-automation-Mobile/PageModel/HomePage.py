from PageModel.BasePage import BasePage
from selenium.webdriver.common.by import By


class TabBar:
    tabBar = (By.LINK_TEXT, 'Toggle SideBar')
    home = (By.LINK_TEXT, 'Home')
    businessUnits = (By.LINK_TEXT, 'Business Units')



class HomePage(BasePage):
    # Check current is the home page
    def checkThisisHomePage(self):
        assert self.if_element_exist(TabBar.home)

    def selectTab(self,tab):
        self.click_element(TabBar.tabBar)
        self.select_by_tab_name(tab)