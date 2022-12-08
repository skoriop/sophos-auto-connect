from selenium import webdriver
from selenium.webdriver import edge

# Replace with your actual username and password
site = 'http://172.16.0.30:8090/httpclient.html'
username = 'xxxxxxxxxxxx'
password = 'xxxxxxxxxxxx'

browser = webdriver.Edge()
browser.get(site)

usernameField = browser.find_element('id', 'username')
usernameField.send_keys(username)

passwordField = browser.find_element('id', 'password')
passwordField.send_keys(password)

submitButton = browser.find_element('id', 'loginbutton')
submitButton.click()

browser.quit()
