from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from utility.wait_utils import WaitUtils
from selenium.webdriver.support.select import Select

class Find(object):
	def __init__(self, driver):
		self.driver = driver
		self.interval = 0.5
		self.timeout = 20

	def find_web_element(self, by, value):
		try:
			WaitUtils.wait_for_element_present(self.driver, (by, value), self.interval, self.timeout)
			return self.driver.find_element(by, value)
		except TimeoutException as e:
			raise NoSuchElementException("Cannot find element by [%s] " % value, e)

	def find_web_elements(self, by, value, until_number):
		last_time = 0.0
		while len(self.driver.find_elements(by, value)) < until_number:
			element_count = len(self.driver.find_elements(by, value))
			sleep(self.interval)
			last_time = last_time + 0.5
			if last_time == self.timeout:
				print("The total elements count do not match the given until number."
					"Totally {} elements found in page, need element count >= {}".format(
					element_count, until_number))
				return None
		return self.driver.find_elements(by, value)

	def select_element(self,element):
		try:
			WaitUtils.wait_for_element_present_element(self.driver,element)
			return Select(element)
		except TimeoutException as e:
			raise NoSuchElementException("Cannot find element by [%s] " % element, e)


