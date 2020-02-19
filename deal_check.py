import time
from selenium import webdriver
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# fetch login credentials from json
with open('creds.json') as credentials:
    data = json.load(credentials)
    
credentials.close()

# login to amazon account
driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.amazon.com/')
time.sleep(1)
sign_in_button = driver.find_element_by_id('nav-signin-tooltip')
sign_in_button.click()
time.sleep(1)
email_input = driver.find_element_by_id('ap_email')
email_input.send_keys(data['Username'])
email_input.submit()
password_input = driver.find_element_by_id('ap_password')
password_input.send_keys(data['Password'])
password_input.submit()
time.sleep(1)

# navigate to List
#hover_menu = driver.find_element(By.XPATH, '//a[text()="Account & Lists"]')
#action = ActionChains(driver)
#action.move_to_element(hover_menu).perform()


driver.quit()
