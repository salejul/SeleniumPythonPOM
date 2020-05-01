import time

from selenium import webdriver
from POMDemoProject.Pages.HomePage import HomePage
from POMDemoProject.Pages.LoginPage import LoginPage
import unittest


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def testLoginValid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login_steps = LoginPage(driver)
        login_steps.enter_username("Admin")
        login_steps.enter_password("admin123")
        login_steps.click_on_login_button()
        home_page_steps = HomePage(driver)
        home_page_steps.click_welcome()
        home_page_steps.click_on_logout()
        time.sleep(4)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")
