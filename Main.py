from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from CreateCard.CreateCard import *
from UpdatePagination.UpdatePagination import *

USERNAME = 'testuser1@example.com'
PASSWORD = 'testuser1@example.com'

class Test(unittest.TestCase):

    def setUp(self):
        self.browser = login_to_create_token(USERNAME, PASSWORD)

    def test_createCard(self):
        print()
        result = test_createCard_method(self.browser)
        self.assertTrue(result, "Тест не пройден")

    def test_updatePagination(self):
        print()
        result = test_UpdatePagination_method(self.browser)
        self.assertTrue(result, "Тест не пройден")

    def tearDown(self):
        self.browser.quit()