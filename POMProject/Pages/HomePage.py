from POMDemoProject.Elements.Elements import Elements as Locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.welcome_link = Locators.welcome_link
        self.logout_linkText = Locators.logout_linkText

    def click_welcome(self):
        self.driver.find_element_by_id(self.welcome_link).click()

    def click_on_logout(self):
        self.driver.find_element_by_link_text(self.logout_linkText).click()
