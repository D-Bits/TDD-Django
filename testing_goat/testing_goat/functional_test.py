from selenium import webdriver
import unittest

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

class NewVisitorTest(unittest.TestCase):

    # Run before each test
    def setup(self):

        self.browser = webdriver.Firefox()

    # Run after each test
    def teardown(self):

        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the Test!')


if __name__ == "__main__":
    
    unittest.main(warnings='ignore')