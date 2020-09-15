from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from globals import chromedriver

def connect_to_opend_chrome(path_to_chrome_driver):
  chrome_options = Options()
  chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
  chrome_driver = path_to_chrome_driver
  driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
  driver.get("http://stackoverflow.com")
  driver.quit()

connect_to_opend_chrome(chromedriver)