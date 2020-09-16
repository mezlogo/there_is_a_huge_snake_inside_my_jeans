from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
from globals import chromedriver

def connect_to_opend_chrome(path_to_chrome_driver):
  chrome_options = Options()
  chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
  chrome_driver = path_to_chrome_driver
  driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
  driver.get("http://stackoverflow.com")
  wait = WebDriverWait(driver, 5, poll_frequency=1, ignored_exceptions=[NoSuchElementException])
  element = wait.until(EC.presence_of_element_located((By.NAME, 'q')))
  driver.quit()

connect_to_opend_chrome(chromedriver)