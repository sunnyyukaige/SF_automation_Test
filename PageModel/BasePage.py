__author__ = 'sunny.yu2'
from selenium.webdriver.common.by import By
from WebElement.Element import Element
from utility.wait_utils import WaitUtils
import time


class Elements:
    Any_api_call_loading = (By.CLASS_NAME, 'test-is-any-api-call-loading')
    Saving_api = (By.CLASS_NAME, 'test-api-saving')
    Previous_session = (By.CLASS_NAME, 'test-nav-previous')
    Button_drop_down = (By.CLASS_NAME, 'test-header-user-dropdown')
    Button_logout = (By.CLASS_NAME, 'test-header-user-log-out')
    Button_confirm_logout = (By.CLASS_NAME, 'ajs-ok')
    Mark_Lighting=(By.TAG_NAME,'mark')
    Closethiswindow = (By.CSS_SELECTOR,"button[title='Close this window']")


class BasePage(Element):
    browser = None

    def __init__(self, browser):
        self.browser = browser

    def getUrl(self):
      return  self.browser.current_url

    def Hard_Sleep(self, seconds):
        time.sleep(seconds)

    def PageDown(self, size=400):
        self.browser.execute_script("window.scrollTo(0, {});".format(size))
        time.sleep(1)

    def PageUp(self):
        self.browser.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)

    def _loading_finish(self):
        try:
            self._loading()
        except Exception as e:
            print(e)

    def _loading(self):
        isLoading = False
        try:
            WaitUtils.wait_for_element_unpresent(self.browser,
                                                 locator=Element.any_api_call_loading,
                                                 timeout=30,
                                                 interval=0.1)
            isLoading = True
        except Exception as e:
            pass
        return isLoading

    def Save_finished(self):
        WaitUtils.wait_for_element_unpresent(self.browser,
                                             locator=Element.saving_api,
                                             timeout=30,
                                             interval=0.1
                                             )

    def Execute_script(self, script):
        self.browser.execute_script(script)

    def Navigate_To(self, url):
        self.browser.open(url)

    def Find_Element_And_Click(self, locator, until_condition=None):
        """
        Do the smart wait and find the element by locator then click
        :param locator: Tuple type like (by, value)
        :param until_condition: The click action will replay until this condition return true
        :return:
        """
        self._loading_finish()
        self.find_element_and_click(self.browser, locator=locator)
        if until_condition:
            while not until_condition:
                time.sleep(1)
                self.find_element_and_click(self.browser, locator=locator)

    def Find_Element_And_GetClassName(self, locator):
        """
        Do the smart wait and find the element by locator then return the class name
        :param locator: Tuple type like (by, value)
        :return: the class name of the element
        """
        self._loading_finish()
        return self.find_element_and_return_class(self.browser, locator=locator)

    def Find_Element_And_Input(self, locator, input_value):
        """
        Do the smart wait and find the element by locator then input the value
        :param locator: Tuple type like (by, value)
        :param input_value: str type value to input
        :return:
        """
        self._loading_finish()
        self.find_element_and_input(self.browser, locator=locator, input_value=input_value)

    def Find_Element_And_Get_Text(self, locator):
        """
        Do the smart wait and find the element by locator then return the text
        :param locator: Tuple type like (by, value)
        :return: the text in the element
        """
        self._loading_finish()
        return self.find_element_and_return_text(self.browser, locator=locator)

    def Is_Element_Exist(self, locator):
        """
        Do the smart wait and try to locate the element
        :param locator: Tuple type like (by, value)
        :return: True or False return type, True means exist, False means not exist after timeout reached
        """
        self._loading_finish()
        return self.is_element_exist(self.browser, locator=locator)

    def Is_Element_Not_Exist(self, locator):
        """
        Do the smart wait and try to find the element is deleted
        :param locator: Tuple type like (by, value)
        :return: True or False return type, True means exist, False means not exist after timeout reached
        """
        self._loading_finish()
        return self.is_element_not_exist(self.browser, locator=locator)

    def Find_Elements(self, locator, until_number=2):
        """
        Return the list of the elements which matching the locator
        :param locator: Tuple type like (by, value)
        :param until_number: Driver will wait until the total count of element reach this number
        :return: List type of webdriver
        """
        self._loading_finish()
        return self.find_elements(self.browser, locator=locator, until_number=until_number)

    def Find_Element(self, locator):
        """
        Return the element which matching the locator
        :param locator: Tuple type like (by, value)
        :return: List type of webdriver
        """
        self._loading_finish()
        return self.find_element(self.browser, locator=locator)

    def Assert_Element_Exist(self, locator):
        """
        Do the smart wait and assert the element is existed or not,
        raise assert exception when it does not exist
        :param locator: Tuple type like (by, value)
        :return:
        """
        self._loading_finish()
        if self.is_element_exist(self.browser, locator=locator):
            pass
        else:
            raise AssertionError('The element does not exist after timeout limitation,'
                                 'The element locator is ByType: {}, ByValue: {}'.format(locator[0], locator[1]))

    def Assert_Element_Not_Exist(self, locator):
        """
        Do the smart wait and assert the element is not existed
        raise assert exception when it exist
        :param locator: Tuple type like (by, value)
        :return:
        """
        self._loading_finish()
        if self.is_element_not_exist(self.browser, locator=locator):
            pass
        else:
            raise AssertionError('The element still exist after timeout limitation,'
                                 'The element locator is ByType: {}, ByValue: {}'.format(locator[0], locator[1]))

    def Drag_Element_To_Point(self, locator, point):
        """
        Drag the element to certain point
        :param locator: Tuple type like (by, value)
        :param point: Tuple type locatin like (100, 200)
        :return:
        """
        self.drag_element_to_point(self.browser, locator=locator, point=point)

    def NavigationPrev(self):
        self.Find_Element_And_Click(self.previous_session)

    def Logout(self):
        self.Find_Element_And_Click(self.button_drop_down)
        self.Find_Element_And_Click(self.button_logout)
        self.Find_Element_And_Click(self.button_confirm_logout)

    def SelectByLabel(self, name, value):
        """
        Do the smart wait and find the element by locator then input the value
        :param name: label name can be part of
        :param value: str type value to select
        :return:
        """
        self._loading_finish()
        element = self.__getLabelElement(name)
        element_brother = element.find_element(By.XPATH, '../following-sibling::td')
        element_select = element_brother.find_element(By.TAG_NAME, 'select')
        select = self.select_element(self.browser, element_select)
        select.select_by_value(value)

    def InputByLabel(self,name,value):
        """
        Do the smart wait and find the element by locator then input the value
        :param name: label name can be part of
        :param value: str type value to input
        :return:
        """
        self._loading_finish()
        element = self.__getLabelElement(name)
        element_brother = element.find_element(By.XPATH, '../following-sibling::td')
        element_input = element_brother.find_element(By.TAG_NAME, 'input')
        element_input.clear()
        element_input.send_keys(value)

    def __getLabelElement(self, name):
        elements = self.Find_Elements((By.TAG_NAME, "label"))
        for element in elements:
            if name in element.text:
                return element
                break


    def SelectByLabelLighting(self, name, value):
        """
        Do the smart wait and find the element by locator then input the value
        :param name: label name can be part of
        :param value: str type value to select
        :return:
        """
        self._loading_finish()
        element = self.__getLabelElement(name)
        element_brother = element.find_element(By.XPATH, '..')
        element_select = element_brother.find_element(By.TAG_NAME, 'input')
        element_select.send_keys(value)
        self.Find_Element_And_Click(Elements.Mark_Lighting)

    def InputByLabelLighting(self,name,value):
        """
        Do the smart wait and find the element by locator then input the value
        :param name: label name can be part of
        :param value: str type value to input
        :return:
        """
        self._loading_finish()
        element = self.__getLabelElement(name)
        element_brother = element.find_element(By.XPATH, '..')
        element_input = element_brother.find_element(By.TAG_NAME, 'input')
        element_input.clear()
        element_input.send_keys(value)

    def ClosethiswindowButtonExist(self):
        self.Find_Element(Elements.Closethiswindow)
        self.Hard_Sleep(2)

