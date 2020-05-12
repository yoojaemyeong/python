from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
#options.arguments('disable-gpu')

driver = webdriver.Chrome('chromedriver',chrome_options=options)

url = "https://www.naver.com"
driver.get(url)

driver.implicitly_wait(3)
driver.get_screenshot_as_file('naver_main_headless.png')
driver.close()