from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

from globals import chromedriver
from globals import path_to_dataset_folder

import pandas as pd


# ----------------------------------
# Connecting to Chrome
def connect_to_opened_chrome(path_to_chrome_driver, port):
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:" + str(port))
    chrome_driver = path_to_chrome_driver
    return webdriver.Chrome(chrome_driver, options=chrome_options)

# ----------------------------------
# Connect by port number and driver path
driver = connect_to_opened_chrome(chromedriver, 9222)
# Set up waiting
main_wait = WebDriverWait(driver, 5, poll_frequency=1, ignored_exceptions=[NoSuchElementException])
# ----------------------------------
# Get Vacancies from HeadHunter
driver.get("https://hh.ru/vacancies/data-scientist")
wait_1 = WebDriverWait(driver, 5, poll_frequency=1, ignored_exceptions=[NoSuchElementException]). \
    until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.vacancy-serp-item")))

num_pages = len(driver.find_elements_by_css_selector("span a.bloko-button"))
vacancies_df = pd.DataFrame()

for i in range(num_pages):
    print("Performing scrapping on page {}".format(str(i+1)))
    vacancies = driver.find_elements_by_css_selector("div.vacancy-serp-item")
    for link in vacancies:
        try:
            element = main_wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a.HH-LinkModifier")))
            link.find_element_by_css_selector("a.HH-LinkModifier").click()
            driver.switch_to.window(driver.window_handles[1])
            element = main_wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-qa=\"vacancy-description\"]")))
            vacancy_content = []

            vacancy_content.append(driver.find_element_by_css_selector("h1.bloko-header-1").text)
            vacancy_content.append(driver.find_element_by_css_selector("a[data-qa=\"vacancy-company-name\"]").text)
            vacancy_content.append(driver.find_element_by_css_selector("p[data-qa=\"vacancy-view-location\"]").text)
            vacancy_content.append(driver.find_element_by_css_selector("span[data-qa=\"vacancy-experience\"]").text)
            vacancy_content.append(
                driver.find_element_by_css_selector("p[data-qa=\"vacancy-view-employment-mode\"]").text)
            vacancy_content.append(driver.find_element_by_css_selector("p.vacancy-salary").text)
            vacancy_content.append(driver.find_element_by_css_selector("p.vacancy-creation-time").text)
            vacancy_content.append(driver.find_element_by_css_selector("div[data-qa=\"vacancy-description\"]").text)
            vacancy_content.append(driver.find_element_by_css_selector("div.bloko-tag-list").text)

            vacancies_df = pd.concat([vacancies_df, pd.Series(vacancy_content)], axis=1)

            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        except (NoSuchElementException, StaleElementReferenceException):
            vacancy_content.append(None)
            vacancies_df = pd.concat([vacancies_df, pd.Series(vacancy_content)], axis=1)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

    main_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.HH-Pager-Controls-Next"))).click()
    print("Went on page {}".format(str(i + 2)))

# This is awful. Need to handle with it more elegant
vacancies = driver.find_elements_by_css_selector("div.vacancy-serp-item")
for link in vacancies:
    try:
        element = main_wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.HH-LinkModifier")))
        link.find_element_by_css_selector("a.HH-LinkModifier").click()
        driver.switch_to.window(driver.window_handles[1])
        element = main_wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-qa=\"vacancy-description\"]")))
        vacancy_content = []

        vacancy_content.append(driver.find_element_by_css_selector("h1.bloko-header-1").text)
        vacancy_content.append(driver.find_element_by_css_selector("a[data-qa=\"vacancy-company-name\"]").text)
        vacancy_content.append(driver.find_element_by_css_selector("p[data-qa=\"vacancy-view-location\"]").text)
        vacancy_content.append(driver.find_element_by_css_selector("span[data-qa=\"vacancy-experience\"]").text)
        vacancy_content.append(
            driver.find_element_by_css_selector("p[data-qa=\"vacancy-view-employment-mode\"]").text)
        vacancy_content.append(driver.find_element_by_css_selector("p.vacancy-salary").text)
        vacancy_content.append(driver.find_element_by_css_selector("p.vacancy-creation-time").text)
        vacancy_content.append(driver.find_element_by_css_selector("div[data-qa=\"vacancy-description\"]").text)
        vacancy_content.append(driver.find_element_by_css_selector("div.bloko-tag-list").text)

        vacancies_df = pd.concat([vacancies_df, pd.Series(vacancy_content)], axis=1)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    except (NoSuchElementException, StaleElementReferenceException):
        vacancy_content.append(None)
        vacancies_df = pd.concat([vacancies_df, pd.Series(vacancy_content)], axis=1)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

print("Scrapping is over. Congratulations!")
# ----------------------------------
# To CSV file
vacancies_df.to_csv(path_to_dataset_folder + 'vacancies_data.csv')

# ----------------------------------
driver.quit()
