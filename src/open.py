from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from globals import chromedriver

def open_chrome_browser(path_to_chrome_driver):
  driver = webdriver.Chrome(path_to_chrome_driver)
  driver.get("http://stackoverflow.com")
  driver.quit()

open_chrome_browser(chromedriver)