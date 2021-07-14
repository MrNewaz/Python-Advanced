from selenium import webdriver

id = 'tasniakk'
password = 'Balsal12'

browser = webdriver.Chrome()
browser.get('http://github.com')


signin_link = browser.find_element_by_link_text('Sign in')
signin_link.click()

username_box = browser.find_element_by_id('login_field')
username_box.send_keys(id)

password_box = browser.find_element_by_id('password')
password_box.send_keys(password)


password_box.submit()

browser.get('https://github.com/MrNewaz')

assert 'Saif Newaz' in browser.page_source
