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
    Mark_Lighting = (By.TAG_NAME, 'mark')
    Closethiswindow = (By.CSS_SELECTOR, "button[title='Close this window']")
    button_lksrch = (By.ID, 'lksrch')


class BasePage(Element):
    browser = None

    def __init__(self, browser):
        self.browser = browser

    # Get current url
    def get_url(self):
        return self.browser.current_url

    # Go to identify url
    def goto_url(self, url):
        self.browser.get(url)

    # Hard sleep
    def Hard_Sleep(self, seconds):
        time.sleep(seconds)

    # Scroll the page to point or size
    def page_down(self, size=400):
        self.browser.execute_script("window.scrollTo(0, {});".format(size))
        time.sleep(1)

    # Scroll back
    def page_up(self):
        self.browser.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)

    # Wait page load
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

    # Wait finish save
    def save_finished(self):
        WaitUtils.wait_for_element_unpresent(self.browser,
                                             locator=Element.saving_api,
                                             timeout=30,
                                             interval=0.1
                                             )

    # Execute JS
    def execute_script(self, script):
        self.browser.execute_script(script)

    # Navigate to url
    def navigate_to(self, url):
        self.browser.open(url)

    # Navigate to previous page
    def navigation_prev(self):
        self.click_element(self.previous_session)

    # Logout the system
    def logout(self):
        self.click_element(self.button_drop_down)
        self.click_element(self.button_logout)
        self.click_element(self.button_confirm_logout)

    def click_element(self, locator, until_condition=None):
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

    def getClassName_element(self, locator):
        """
        Do the smart wait and find the element by locator then return the class name
        :param locator: Tuple type like (by, value)
        :return: the class name of the element
        """
        self._loading_finish()
        return self.find_element_and_return_class(self.browser, locator=locator)

    def input_element(self, locator, input_value):
        """
        Do the smart wait and find the element by locator then input the value
        :param locator: Tuple type like (by, value)
        :param input_value: str type value to input
        :return:
        """
        self._loading_finish()
        self.find_element_and_input(self.browser, locator=locator, input_value=input_value)

    def get_text_element(self, locator):
        """
        Do the smart wait and find the element by locator then return the text
        :param locator: Tuple type like (by, value)
        :return: the text in the element
        """
        self._loading_finish()
        return self.find_element_and_return_text(self.browser, locator=locator)

    def if_element_exist(self, locator):
        """
        Do the smart wait and try to locate the element
        :param locator: Tuple type like (by, value)
        :return: True or False return type, True means exist, False means not exist after timeout reached
        """
        self._loading_finish()
        return self.is_element_exist(self.browser, locator=locator)

    def element_not_exist(self, locator):
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

    def assert_element_exist(self, locator):
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

    def assert_element_not_exist(self, locator):
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

    def drag_element(self, locator, point):
        """
        Drag the element to certain point
        :param locator: Tuple type like (by, value)
        :param point: Tuple type locatin like (100, 200)
        :return:
        """
        self.drag_element_to_point(self.browser, locator=locator, point=point)

    def select_by_label(self, name, value):
        """
        Do the smart wait and find the element by locator then input the value
        :param name: label name can be part of
        :param value: str type value to select
        :return:
        """
        self._loading_finish()
        element = self._get_label_element(name)
        element_brother = element.find_element(By.XPATH, '../following-sibling::td')
        element_select = element_brother.find_element(By.TAG_NAME, 'select')
        select = self.select_element(self.browser, element_select)
        select.select_by_value(value)

    def input_by_label(self, name, value):
        """
        Do the smart wait and find the element by locator then input the value
        :param name: label name can be part of
        :param value: str type value to input
        :return:
        """
        self._loading_finish()
        element = self._get_label_element(name)
        element_brother = element.find_element(By.XPATH, '../following-sibling::td')
        element_input = element_brother.find_element(By.TAG_NAME, 'input')
        element_input.clear()
        element_input.send_keys(value)

    def search_input_by_label(self, name, value):
        """
        Do the smart wait and find the element by locator then input the value
        :param name: label name can be part of
        :param value: str type value to input
        :return:
        """
        self._loading_finish()
        element = self._get_label_element(name)
        element_brother = element.find_element(By.XPATH, '../following-sibling::td')
        element_input = element_brother.find_element(By.CSS_SELECTOR, 'span>input')
        element_input.clear()
        element_input.send_keys(value)

    # Get element by label
    def _get_label_element(self, name):
        return self._get_element_by_tag_value('label', name)

    def select_by_label_lighting(self, name, value):
        """
        Do the smart wait and find the element by locator then input the value
        :param name: label name can be part of
        :param value: str type value to select
        :return:
        """
        self._loading_finish()
        element = self._get_label_element(name)
        element_brother = element.find_element(By.XPATH, '..')
        element_select = element_brother.find_element(By.TAG_NAME, 'input')
        element_select.send_keys(value)
        self.click_element(Elements.Mark_Lighting)

    def input_by_label_lighting(self, name, value):
        """
        Do the smart wait and find the element by locator then input the value
        :param name: label name can be part of
        :param value: str type value to input
        :return:
        """
        self._loading_finish()
        element = self._get_label_element(name)
        element_brother = element.find_element(By.XPATH, '..')
        element_input = element_brother.find_element(By.TAG_NAME, 'input')
        element_input.clear()
        element_input.send_keys(value)

    # Wait close the window button exist
    def close_this_window_button_exist(self):
        self.Find_Element(Elements.Closethiswindow)
        self.Hard_Sleep(2)

    def switch_to_iframe(self, name):
        """
        Switch to the frame
        :param name: the iframe name or id or class
        :return:
        """
        self.browser.switch_to_frame(name)

    # Switch back from iframe to default content
    def switch_back(self):
        self.browser.switch_to_default_content()

    def _get_element_by_tag_value(self, tag, value):
        elements = self.Find_Elements((By.TAG_NAME, tag))
        for element in elements:
            if value in element.text:
                return element
                break

    def select_button(self, value):
        """
        Select by button and button value
        :param value: the name of button
        :return:
        """
        return self._get_element_by_tag_value('button', value)

    # Generate the random suffix by current datetime
    def generate_random_suffix(self):
        suffix = time.strftime('%y-%m-%d-%H-%M', time.localtime(time.time()))
        return suffix

    def search_by_icon(self, name):
        """
        Search the element by icon name
        :param value: the name of button
        :return:
        """
        self.click_element((By.CSS_SELECTOR, name + ' Lookup (New Window)'))
        self.click_element(Elements.button_lksrch)
        self.Hard_Sleep(30)
