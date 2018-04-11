from PageModel.BasePage import BasePage
from selenium.webdriver.common.by import By


class TabBar:
    tabBar = (By.ID, 'tabBar')
    home = (By.LINK_TEXT, 'Home')
    businessUnits = (By.LINK_TEXT, 'Business Units')
    Investors = (By.LINK_TEXT,'Investors')
    tabMenu=(By.ID,'tsidButton')
    tabLabel=(By.ID,'tsidLabel')
    tabLink=(By.CLASS_NAME,'menuButtonMenuLink')
    switch_to_lightning=(By.CLASS_NAME,"switch-to-lightning")
    appLauncher=(By.CLASS_NAME,'slds-icon-waffle_container')
    tabIcon=(By.CLASS_NAME,'appTileTitleNoDesc')

class HomePage(BasePage):


    def checkThisisHomePage(self):
        assert self.Is_Element_Exist(TabBar.home)

    def gotoBU(self):
        self.Find_Element_And_Click(TabBar.businessUnits)

    def gotoInvestors(self):
        self.Find_Element_And_Click(TabBar.Investors)

    def gotoTab(self,name):
        label=self.Find_Element_And_Get_Text(TabBar.tabLabel)
        if(name not in label):
            self.Find_Element_And_Click(TabBar.tabMenu)
            elements=self.Find_Elements(TabBar.tabLink)
            for s in elements:
                if name in s.text:
                    s.click()
                    break

        else:
            pass

    def switch_to_lightning(self):
        url=self.getUrl()
        if('lightning' not in url):
            self.Find_Element_And_Click(TabBar.switch_to_lightning)

    def gotoModule(self,value):
        self.Hard_Sleep(5)
        self.Find_Element_And_Click(TabBar.appLauncher)
        self.Hard_Sleep(5)
        elements=self.Find_Elements(TabBar.tabIcon)
        for element in elements:
            if(value in element.text):
                element.click()
                break

    def gotoLightTab(self,value):
        self.Find_Element_And_Click((By.CSS_SELECTOR,"a[title='"+value+"']"))
        while value not in self.browser.title:
            self.Hard_Sleep(1)
