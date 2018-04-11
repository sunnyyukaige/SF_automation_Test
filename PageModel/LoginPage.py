__author__ = 'sunny.yu2'
from PageModel.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
	# PageObject definition
	input_username = (By.ID, 'username')
	input_password = (By.ID, 'password')
	button_signin = (By.ID, 'Login')


	def userName(self, value):
		self.Find_Element_And_Input(self.input_username, value)

	def password(self, value):
		self.Find_Element_And_Input(self.input_password, value)

	def signIn(self):
		self.Find_Element_And_Click(self.button_signin)
