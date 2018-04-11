from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitUtils(object):
    interval = 0.5
    timeout = 30.0

    @staticmethod
    def wait_for_element_present(driver, locator, interval=interval, timeout=timeout):
        return WebDriverWait(driver, timeout, interval).until(EC.presence_of_all_elements_located(locator))

    @staticmethod
    def wait_for_element_visible(driver, locator, interval=interval, timeout=timeout):
        return WebDriverWait(driver, timeout, interval).until(EC.visibility_of_all_elements_located(locator))

    @staticmethod
    def wait_for_element_clickable(driver, locator, interval=interval, timeout=timeout):
        return WebDriverWait(driver, timeout, interval).until(EC.element_to_be_clickable(locator))

    @staticmethod
    def wait_for_element_unpresent(driver, locator, interval=interval, timeout=timeout):
        return WebDriverWait(driver, timeout, interval).until_not(EC.presence_of_all_elements_located(locator))


    @staticmethod
    def wait_for_element_present_element(driver, element, interval=interval, timeout=timeout):
        return WebDriverWait(driver, timeout, interval).until(EC.visibility_of(element))
