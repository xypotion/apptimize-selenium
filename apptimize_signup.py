# explicit requirements:
# sign up for 30-day trial account at apptimize.com
# use "Apptimize Candidate" for company
# record all email addresses used to sign up

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

def newEmail(testName):
    return "maxawunderlich+{0}{1}@gmail.com".format(testName, int(time.time()))

driver = webdriver.Firefox()

# go straight to trial signup page, since that's faster than loading apptimize.com first and clicking Sign Up
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
email.send_keys(newEmail("TrialSignup"))

company = driver.find_element_by_id("company")
company.clear()
company.send_keys("Apptimize Candidate")

password = driver.find_element_by_id("password")
password.clear()
password.send_keys("password%d" % int(time.time()))

# click "No" for "Have you purchased a software platform in the last 6 months?"
purchasedNo = driver.find_element_by_xpath('//input[@name="purchased"][@value="No"]')
purchasedNo.click()

# click Terms & Conditions checkbox
eula = driver.find_element_by_id("eula")
eula.click()

# # assert "No results found." not in driver.page_source
# assert "Event" not in driver.page_source

# driver.close()