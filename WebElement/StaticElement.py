from WebElement.Element import Element


class StaticElement(Element):

    def __init__(self, parent ,by, value,current_element=None):
        Element.__init__(self)
        self.current_element = current_element
        self.by = by
        self.value = value
        self.parent = parent

    def _selenium_context(self):
        if not self.current_element:
            self._refresh()
        return self.current_element



    def _refresh(self):
        print("We are refreshed.")
        self.current_element = self.parent.find_element(self.by, self.value)



