from WebElement.By import By
from WebElement.Element import Element




class DynamicElement(Element):

    def __init__(self, parent, element, identifier=None):
        Element.__init__(self)
        self.current_element = element
        self.identifier = identifier
        self.parent = parent
        self.value_of_identifier = None

    def _selenium_context(self):
        return self.current_element


    def _refresh(self):
        if not self.identifier:
            pass
        else:
            self.current_element = self.parent.find_element(self._convert_to_by(self.identifier), self.current_element.get_attribute(self.identifier))


    #TODO: Will find a good way to resolve the problem of refresh dynamic element.
    def _convert_to_by(self):
        # if self.identifier.lower() == "xpath":
        #     return By.XPATH

        if self.identifier.lower() == "id":
            return By.ID

        if self.identifier.lower() == "class_name":
             return By.CLASS_NAME

        if self.identifier.lower() == "name":
            return By.NAME

        # if self.identifier.lower() == "ios_uiautomation":
        #     return By.IOS_UIAUTOMATION

        # if self.identifier.lower() == "accessibility_id":
        #     return By.ACCESSIBILITY_ID


