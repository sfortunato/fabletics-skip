#!/usr/bin/env python
# from xml import xpath
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options 

from credentials import username, password


def get_profile():
    profile = FirefoxProfile()
    # Disable CSS
    # profile.set_preference('permissions.default.stylesheet', 2)
    # Disable images
    # profile.set_preference('permission.default.image', 2)
    # Disable Flash
    profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so','false')

    return profile

def run():
    profile = get_profile()
    options = Options()
    # options.add_argument("--headless")
    driver = webdriver.Firefox(firefox_profile=profile, options=options)
    driver.implicitly_wait(30)

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

    html = driver.page_source()
    if "Susanne" in html:
        print("logged in successfully")
    else:
        print("try again")

    driver.quit()

if __name__ == '__main__':
    run()



# driver.find_element_by_id("name of id").click()
# driver.get("url")

# Button html
# <button class="button" data-role="none" type="submit">Sign In</button>
# driver.findElement(By.xpath("//button[text()='Confirm']")).click();
# driver.find_elements_by_xpath("//*[contains(text(), 'My Button')]")

# driver.findElement(By.linkText("Log in")):

'''
Modal: button to x-out of modal id = 'cboxClose' --> may vary significantlly
'sign in' find by link text 'Sign In'
alt: just go straight to https://www.fabletics.com/index.cfm?action=home.login

Alternate URL to login login, skip modal: https://www.fabletics.com/index.cfm?action=home.login 


'''

