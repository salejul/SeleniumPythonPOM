from POMDemoProject.Elements.Elements import Elements as Locators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_textBox = Locators.username_textBox
        self.password_textBox = Locators.password_textBox
        self.loginButton = Locators.loginButton

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textBox).clear()
        self.driver.find_element_by_id(self.username_textBox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textBox).clear()
        self.driver.find_element_by_id(self.password_textBox).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element_by_id(self.loginButton).click()


