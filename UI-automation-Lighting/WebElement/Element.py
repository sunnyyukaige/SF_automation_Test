from time import sleep
from selenium.common.exceptions import *
from utility.find import Find
from utility.wait_utils import WaitUtils
from selenium.webdriver.common.action_chains import ActionChains


class Element(object):
    @staticmethod
    def find_element_and_click(driver, locator):
        try:
            Find(driver).find_web_element(locator[0], locator[1]).click()
        except WebDriverException as Retry:
            sleep(2)
            Find(driver).find_web_element(locator[0], locator[1]).click()

    @staticmethod
    def find_element_and_input(driver, locator, input_value):
        Find(driver).find_web_element(locator[0], locator[1]).clear()
        Find(driver).find_web_element(locator[0], locator[1]).send_keys(input_value)

    @staticmethod
    def find_element_and_return_text(driver, locator):
        return Find(driver).find_web_element(locator[0], locator[1]).text

    @staticmethod
    def find_element_and_return_class(driver, locator):
        return Find(driver).find_web_element(locator[0], locator[1]).get_attribute('class')

    @staticmethod
    def is_element_exist(driver, locator):
        try:
            WaitUtils.wait_for_element_visible(driver=driver,
                                               locator=locator
                                               )
            return True
        except TimeoutException:
            return False

    @staticmethod
    def is_element_not_exist(driver, locator):
        try:
            WaitUtils.wait_for_element_unpresent(driver=driver,
                                                 locator=locator
                                                 )
            return True
        except TimeoutException:
            return False

    @staticmethod
    def find_elements(driver, locator, until_number):
        return Find(driver).find_web_elements(locator[0], locator[1], until_number=until_number)

    @staticmethod
    def drag_element_to_point(driver, locator, point):
        element = Find(driver).find_web_element(locator[0], locator[1])
        ActionChains(driver).click_and_hold(element).move_by_offset(point[0], point[1]).release().perform()


    @staticmethod
    def find_element(driver, locator):
        return Find(driver).find_web_element(locator[0], locator[1])

    @staticmethod
    def select_element(driver,element):
        return Find(driver).select_element(element)

