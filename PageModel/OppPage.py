__author__ = 'sunny.yu2'
from PageModel.BasePage import BasePage
from selenium.webdriver.common.by import By
import time


class OppPage(BasePage):
    # PageObject Definition

    button_quote = (By.CSS_SELECTOR, "input[value='Quote']")
    iframe_button = (By.CSS_SELECTOR, "iframe[title='OpportunityButton']")
    button_new = (By.NAME, 'new')

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
        time.sleep(60)

    # Fill the BU value
    def fillBU(self):
        self.search_input_by_label('Business Unit', 'Indonesia Franchise')

    # Fill the center info
    def fillCenter(self):
        self.search_input_by_label('Center', 'Lombok')

    # Fill the stage value
    def selectStage(self):
        self.select_by_label('Stage', 'Showed Up')

    # Set the Target close date
    def setTargetCloseDate(self):
        self.search_input_by_label('Target Close Date', '2018-4-20')
