__author__ = 'sunny.yu2'
from PageModel.BasePage import BasePage
from selenium.webdriver.common.by import By
import time


class OppPage(BasePage):
    # PageObject Definition

    button_quote = (By.CSS_SELECTOR, "input[value='Quote']")
    iframe_button = (By.CSS_SELECTOR, "iframe[title='OpportunityButton']")
    button_new = (By.NAME, 'new')
    button_save = (By.NAME, 'save')

    # Goto quote page
    def goto_quote(self):
        iframe = self.Find_Element(self.iframe_button)
        self.switch_to_iframe(iframe)
        self.click_element(self.button_quote)
        self.switch_back()
        # Create new button

    def creat_new_button(self):
        self.click_element(self.button_new)

    # Fill the name of opp
    def fill_oppName(self):
        self.input_by_label('Opportunity Name', 'sunny' + self.generate_random_suffix())

    # Fill the BU value
    def fillBU(self):
        self.search_input_by_label_with_span('Business Unit', 'Indonesia Franchise')

    # Fill the center info
    def fillCenter(self):
        self.search_input_by_label('Center', 'Lombok')

    # Fill the stage value
    def selectStage(self, value):
        self.select_by_label('Stage', value)

    # Set the Target close date
    def setTargetCloseDate(self, time):
        self.search_input_by_label('Target Close Date', time)

    # Save the opp content
    def save(self):
        self.click_element(self.button_save)

    # Select account name
    def selectAccountName(self, value):
        self.search_by_icon('Account Name', value)
