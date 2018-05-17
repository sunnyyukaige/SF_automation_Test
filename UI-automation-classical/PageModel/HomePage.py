from PageModel.BasePage import BasePage
from selenium.webdriver.common.by import By


class TabBar:
    tabBar = (By.ID, 'tabBar')
    home = (By.LINK_TEXT, 'Home')
    businessUnits = (By.LINK_TEXT, 'Business Units')
    Investors = (By.LINK_TEXT, 'Investors')
    tabMenu = (By.ID, 'tsidButton')
    tabLabel = (By.ID, 'tsidLabel')
    tabLink = (By.CLASS_NAME, 'menuButtonMenuLink')
    switch_to_lightning = (By.CLASS_NAME, "switch-to-lightning")
    appLauncher = (By.CLASS_NAME, 'slds-icon-waffle_container')
    tabIcon = (By.CLASS_NAME, 'appTileTitleNoDesc')
    profileIcon = (By.CSS_SELECTOR, "span.photoContainer.forceSocialPhoto")
    swith_to_classical = (By.LINK_TEXT, 'Switch to Salesforce Classic')
    opp = (By.LINK_TEXT, 'Opportunities')


class HomePage(BasePage):
    # Check current is the home page
    def checkThisisHomePage(self):
        assert self.if_element_exist(TabBar.home)

    # Go to bu
    def gotoBU(self):
        self.click_element(TabBar.businessUnits)

    # Go to Opp
    def gotoOpp(self):
        self.click_element(TabBar.opp)

    # Go to Investors
    def gotoInvestors(self):
        self.click_element(TabBar.Investors)

    def goto_tab(self, name):
        """
        Go to the tab you want by name
        :param name: the name of tab
        :return:
        """
        label = self.get_text_element(TabBar.tabLabel)
        if (name not in label):
            self.click_element(TabBar.tabMenu)
            elements = self.Find_Elements(TabBar.tabLink)
            for s in elements:
                if name in s.text:
                    s.click()
                    break

        else:
            pass
        # Switch to lighting module

    def switch_to_lightning(self):
        url = self.get_url()
        if ('lightning' not in url):
            self.click_element(TabBar.switch_to_lightning)

    def goto_module(self, value):
        """
        Goto module by name of module
        :param value: the name of module
        :return:
        """
        self.Hard_Sleep(5)
        self.click_element(TabBar.appLauncher)
        self.Hard_Sleep(5)
        elements = self.Find_Elements(TabBar.tabIcon)
        for element in elements:
            if (value in element.text):
                element.click()
                break

    def goto_tab_lighting(self, value):
        """
        Search the element by icon name
        :param value: the name of button
        :return:
        """
        self.click_element((By.CSS_SELECTOR, "a[title='" + value + "']"))
        while value not in self.driver.title:
            self.Hard_Sleep(1)
        # Switch to classical module

    def switch_to_classical(self):
        url = self.get_url()
        if ('lightning' in url):
            self.click_element(TabBar.profileIcon)
            self.click_element(TabBar.swith_to_classical)
