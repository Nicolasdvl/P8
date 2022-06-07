from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from django.test import override_settings
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from dotenv import load_dotenv
import os
import unittest


@unittest.skipIf(bool(os.environ.get("CI")))
@override_settings(
    STATICFILES_STORAGE="django.contrib.staticfiles.storage.StaticFilesStorage"
)
class TestSelenium(StaticLiveServerTestCase):
    """End to end tests."""

    fixtures = [
        "test_users.json",
        "test_products.json",
        "test_categories.json",
    ]

    @classmethod
    def setUpClass(cls):
        """Set up fixtures and launch driver before running tests."""
        load_dotenv()
        super().setUpClass()
        options = Options()
        options.add_argument("start-maximized")
        options.binary_location = os.getenv("BROWSER_LOCATION")
        cls.driver = webdriver.Chrome(
            executable_path=os.getenv("DRIVER_PATH"),
            options=options,
        )

    @classmethod
    def tearDownClass(cls):
        """Deconstruct fixtures and quit driver after running tests."""
        cls.driver.quit()
        super().tearDownClass()

    def test_login_logout(self):
        """Test user path"""
        self.driver.get(f"{self.live_server_url}/")
        self.assertEqual(self.driver.current_url, f"{self.live_server_url}/")
        self.driver.find_element_by_name("login").click()
        email_input = self.driver.find_element_by_name("email")
        email_input.send_keys("john@email.com")
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys("mdp")
        self.driver.find_element_by_name("submit_logs").click()
        # Test if current url is home page
        self.assertEqual(self.driver.current_url, f"{self.live_server_url}/")
        self.driver.find_element_by_name("my_account")
        self.driver.find_element_by_name("logout").click()
        # Test if current url is home page
        self.assertEqual(self.driver.current_url, f"{self.live_server_url}/")
        try:
            self.driver.find_element_by_name("my_account")
        except NoSuchElementException:
            pass
        else:
            raise ValueError("my account should not be visible")

    def test_create_account(self):
        self.driver.get(f"{self.live_server_url}/")
        self.driver.find_element_by_name("signup").click()
        # Give already existing username and email
        email_input = self.driver.find_element_by_name("username")
        email_input.send_keys("john")
        password_input = self.driver.find_element_by_name("email")
        password_input.send_keys("john@email.com")
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys("mdp")
        password_input = self.driver.find_element_by_name("confirme")
        password_input.send_keys("mdp")
        self.driver.find_element_by_name("submit_new_user").click()
        # Test if current url is signup page
        self.assertEqual(
            self.driver.current_url, f"{self.live_server_url}/signup"
        )
        # Test if username error was genarated
        # self.driver.find_element_by_id("error_1_id_username")
        # Test if email error was genarated
        # self.driver.find_element_by_id("error_1_id_email")
        # Give new user info
        email_input = self.driver.find_element_by_name("username")
        email_input.send_keys("john83")
        password_input = self.driver.find_element_by_name("email")
        password_input.send_keys("john83@email.com")
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys("mdp")
        password_input = self.driver.find_element_by_name("confirme")
        password_input.send_keys("mdp")
        self.driver.find_element_by_name("submit_new_user").click()

    def test_add_substitutes(self):
        self.driver.get(f"{self.live_server_url}/")
        self.driver.find_element_by_name("login").click()
        # Login with user who doesn't have substitutes saved
        email_input = self.driver.find_element_by_name("email")
        email_input.send_keys("jack@email.com")
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys("azert")
        self.driver.find_element_by_name("submit_logs").click()
        # Search for a product, here 'coca'
        self.driver.find_element_by_name("search_input").send_keys("coca")
        # Click on first element in auto-complete list
        self.driver.find_element_by_xpath(
            "//div[@id='search_inputautocomplete-list']/div[1]"
        ).click()
        self.driver.find_element_by_id("submit_search").click()
        # Save the first substitute found
        self.driver.find_element_by_xpath(
            "//div[@class='product_container'][1]//button[@name='submit_save']"
        ).click()
        # Check if previous save is at user saves page, here pepsi max.
        self.driver.find_element_by_name("my_substitutes").click()
        self.assertTrue("pepsi max" in self.driver.page_source)
