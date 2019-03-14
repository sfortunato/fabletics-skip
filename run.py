#!/usr/bin/env python
# from xml import xpath
import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options 

from credentials import username, password



def safe_clear_modal(driver):
    print("in safe_clear_modal")
    try:
        print("in try")
        modal_x = driver.find_element_by_id("cboxClose")
        modal_x.click()
        return True
    except:
        print('in except')
        return False 


def skip_month(driver):
    pass


def log_in(driver):
    link = "https://www.fabletics.com/index.cfm?action=home.login"
    driver.get(link)
    driver.implicitly_wait(30)

    # Enter username
    driver.find_element_by_id("reference_data").send_keys(username)
    # Enter password
    driver.find_element_by_id("verification_data").send_keys(password)
    # Click login button
    # driver.findElement(By.linkText("Sign In"))
    driver.find_element_by_id("submitSignIn").click()
    driver.implicitly_wait(30)

    return driver


def get_profile():
    profile = FirefoxProfile()
    # Disable CSS
    # profile.set_preference('permissions.default.stylesheet', 2)
    # Disable images
    # profile.set_preference('permission.default.image', 2)
    # Disable Flash
    profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so','false')

    return profile

def get_webdriver():
    profile = get_profile()
    options = Options()
    # options.add_argument("--headless")
    driver = webdriver.Firefox(firefox_profile=profile, options=options)
    driver.implicitly_wait(30)

    return driver


def run():

    driver = get_webdriver()

    log_in(driver)
    time.sleep(4)
    safe_clear_modal(driver)
    time.sleep(4)
    skip_month(driver)

    driver.quit()

if __name__ == '__main__':
    run()


