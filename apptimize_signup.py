# tests for https://apptimize.com/30-day-trial

import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class ApptimizeTrialSignupPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 5)

    # ensures that a new user can sign up for a 30-day trial account
    def test_trial_signup_basic(self):
        driver = self.driver
        wait = self.wait
        
        newEmail = self.newEmail("TrialSignup")
        newPassword = "password%d" % int(time.time())
        
        # there's probably a better way of logging this, but this works for now
        print(newEmail, newPassword)

        driver.get("https://apptimize.com/30-day-trial")

        # fill in required fields in signup form
        fname = driver.find_element_by_id("fname")
        fname.clear()
        fname.send_keys("Max")

        lname = driver.find_element_by_id("lname")
        lname.clear()
        lname.send_keys("Wunderlich")

        email = driver.find_element_by_id("email")
        email.clear()
        email.send_keys(newEmail)

        company = driver.find_element_by_id("company")
        company.clear()
        company.send_keys("Apptimize Candidate")

        password = driver.find_element_by_id("password")
        password.clear()
        password.send_keys(newPassword)

        # click "No" for "Have you purchased a software platform in the last 6 months?"
        purchasedNo = driver.find_element_by_xpath('//input[@name="purchased"][@value="No"]')
        purchasedNo.click()

        # click Terms & Conditions checkbox
        eula = driver.find_element_by_id("eula")
        eula.click()

        # click submit button
        submit = driver.find_element_by_id("submit")
        submit.click()

        # success = user lands on Create App page. seems a little slow (or uses AJAX), so waiting here instead of asserting
        wait.until(expected_conditions.title_contains("Create App"))

    def tearDown(self):
        self.driver.close()

    def newEmail(self, testName):
        return "maxawunderlich+{0}{1}@gmail.com".format(testName, int(time.time()))

if __name__ == "__main__":
    unittest.main()