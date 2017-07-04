# explicit requirements:
# sign up for 30-day trial account at apptimize.com
# use "Apptimize Candidate" for company
# record all email addresses used to sign up

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

def newEmail(testName):
    return "maxawunderlich+{0}{1}@gmail.com".format(testName, int(time.time()))

print(newEmail("TrialSignup"))

# driver = webdriver.Firefox()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# # assert "No results found." not in driver.page_source
# assert "Event" not in driver.page_source
# driver.close()