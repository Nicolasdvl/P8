from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from dotenv import load_dotenv
import os


class TestSelenium(StaticLiveServerTestCase):
    """"""

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
        self.driver.get(f"{self.live_server_url}/")
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
        self.driver.find_element_by_id("error_1_id_username")
        # Test if email error was genarated
        self.driver.find_element_by_id("error_1_id_email")
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
        # Test if current url is home page
        self.driver.implicitly_wait(5)
        self.assertEqual(self.driver.current_url, f"{self.live_server_url}/")
        self.driver.find_element_by_name("logout").click()

    def test_add_substitutes(self):
        self.driver.get(f"{self.live_server_url}/")
        self.driver.find_element_by_name("login").click()
        # Login
        email_input = self.driver.find_element_by_name("email")
        email_input.send_keys("john@email.com")
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys("mdp")
        self.driver.find_element_by_name("submit_logs").click()
        # Search for a product, here 'Coca-Cola'
        self.driver.find_element_by_name("search_input").send_keys("Nutella")
        self.driver.find_element_by_xpath("submit_search").click()
        # Save the first substitute found, it should be 'Coca Zéro'
        self.driver.find_element_by_xpath(
            "//div[@class='product_container'][1]//button[@name='submit_save']"
        ).click()
        # Check if previous save is at user saves page.
        self.driver.find_element_by_name("my_substitutes").click()
        self.assertTrue("Nocciolata" in self.driver.page_source)
        # Vérifier le nom sauvegardé en fonction
        # du nom produit récupéré dans la page substitutes
