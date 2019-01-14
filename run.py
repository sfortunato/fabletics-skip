#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


def get_profile():
    profile = FirefoxProfile()
    # Disable CSS
    profile.set_preference('permissions.default.stylesheet', 2)
    # Disable images
    profile.set_preference('permission.default.image', 2)
    # Disable Flash
    profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so','false')

    return profile

def run():
    profile = get_profile()
    driver = webdriver.Firefox(profile)
    driver.implicitly_wait(30)

    link = "https://www.fabletics.com/"
    driver.get(link)
    driver.implicitly_wait(30)

    results = {
        'url': driver.current_url,
        'source': driver.page_source

    }

    driver.quit()
    return results

if __name__ == '__main__':
    run()

