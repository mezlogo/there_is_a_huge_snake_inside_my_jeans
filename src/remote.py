from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from functional import seq
from globals import chromedriver

import pandas as pd


#Example of listing all content from plain files in github with ajax requests

def connect_to_opened_chrome(path_to_chrome_driver, port):
  chrome_options = Options()
  chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:" + str(port))
  chrome_driver = path_to_chrome_driver
  return webdriver.Chrome(chrome_driver, options=chrome_options)

#connect by port number and driver path
driver = connect_to_opened_chrome(chromedriver, 9222)
#go to project page

# Origin code - Github repo interspection
# ----------------------------------
# driver.get("https://github.com/mezlogo/there_is_a_huge_snake_inside_my_jeans")
# arrayOfWebElements = driver.find_elements_by_css_selector("div.Details div.Box-row")
#get list of all files in repository
#you can test this query by javascript console in browser `document.querySelectorAll("div.Details div.Box-row")`
#convert to PyFunctional seq https://github.com/EntilZha/PyFunctional
# ----------------------------------
# elems = seq(arrayOfWebElements)
#print pairs of file name and file type (dir of plain file)
#example for js with only file name
# document.querySelectorAll("div.Details div.Box-row")[0].querySelector("a[title]").getAttribute("title")
#example with pair of type and title
# Array.from(document.querySelectorAll("div.Details div.Box-row")).map(elem => "title: " + elem.querySelector("svg[aria-label]").getAttribute("aria-label") + " type: " + elem.querySelector("a[title]").getAttribute("title"))
# ----------------------------------
# Origin code - Github repo interspection
# print(elems.map(lambda elem:
#     "type: " +
#     elem.find_element_by_css_selector("svg[aria-label]").get_attribute("aria-label")
#     + " titile: " +
#     elem.find_element_by_css_selector("a[title]").get_attribute("title"))
# )

# ----------------------------------
# Example 1
# StackOverflow: Gradient Descent question - votes count
# driver.get("https://stackoverflow.com/questions/17784587/gradient-descent-using-python-and-numpy")
# ----------------------------------
# Additional test-links:
# driver.get("https://stackoverflow.com/questions/28253102/python-3-multiply-a-vector-by-a-matrix-without-numpy")
# driver.get("https://stackoverflow.com/questions/9537392/git-fetch-remote-branch")
# ----------------------------------
# topic_title = driver.find_elements_by_css_selector("div#question-header")
# topic_tags = driver.find_elements_by_css_selector("div.post-taglist a.post-tag")
# arrayOfWebElements = driver.find_elements_by_css_selector("div.votecell")
# elems = seq(arrayOfWebElements)
# ----------------------------------
# print(seq(topic_title).map(lambda title:
#     title.find_element_by_css_selector("a.question-hyperlink").get_attribute("text"))[0], '\n', \
#     "Topic tags: ", seq(topic_tags).map(lambda tag:
#     tag.get_attribute("text")), '\n', \
#     elems.map(lambda elem: "Topic-starter_votes: " +
#     elem.find_element_by_css_selector("div.js-vote-count").get_attribute("data-value"))[0], \
#     '\n', "Answers_votes:",\
#     elems.map(lambda elem: elem.find_element_by_css_selector("div.js-vote-count").get_attribute("data-value"))[1:]
# )
# ----------------------------------
# Example 2
# Compare Vacancies from HeadHunter
# driver.get("https://spb.hh.ru/vacancies/data-scientist")
# wait = WebDriverWait(driver, 5, poll_frequency=1, ignored_exceptions=[NoSuchElementException]). \
#     until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.vacancy-serp-item")))
# vacancies = driver.find_elements_by_css_selector("div.vacancy-serp-item")
#
# list_of_vacancies = []
#
# for vacancy in seq(vacancies):
#     try:
#         list_of_vacancies.append(vacancy.find_element_by_css_selector("a.HH-LinkModifier").get_attribute("text"))
#         list_of_vacancies.append(vacancy.find_element_by_css_selector("a[data-qa=\"vacancy-serp__vacancy-employer\"]").get_attribute("text"))
#         list_of_vacancies.append(vacancy.find_element_by_css_selector("div.g-user-content").text)
#         list_of_vacancies.append(vacancy.find_element_by_css_selector("span[data-qa=\"vacancy-serp__vacancy-compensation\"]").text)
#
#     except NoSuchElementException:
#         list_of_vacancies.append(None)
#
# separated_vacancies = [list_of_vacancies[x:x+4] for x in range(0, len(list_of_vacancies), 4)]
# print(*separated_vacancies)

# ----------------------------------
# Example 3
# Explore some vacancy from HeadHunter
# for link in vacancies[0:1]: # there's 50 vacancies on the page - let's test on some
#     link.find_element_by_css_selector("a.HH-LinkModifier").click()
#     driver.switch_to.window(driver.window_handles[0])
#
# for handle in driver.window_handles[1:]:
#     driver.switch_to.window(handle)

driver.get("https://spb.hh.ru/vacancy/39110818?query=data%20scientist")
vacancy_title = driver.find_element_by_css_selector("h1.bloko-header-1")
vacancy_salary = driver.find_element_by_css_selector("p.vacancy-salary")
vacancy_description = driver.find_element_by_css_selector("div[data-qa=\"vacancy-description\"]")
vacancy_tags = driver.find_element_by_css_selector("div.bloko-tag-list")

vacancy_content = [vacancy_title.text, vacancy_salary.text, vacancy_description.text, vacancy_tags.text]

vacancies = pd.DataFrame(data=vacancy_content, index=['vacancy_title', 'vacancy_salary', 'vacancy_description', 'vacancy_tags']).T
vacancies.to_csv('D:\\PyCharm_Projects\\Created DataFrames\\vacancies_data.csv', encoding="cp1251")

# v = pd.read_csv('D:\\PyCharm_Projects\\Created DataFrames\\vacancies_data.csv', encoding="cp1251", index_col=False)
# print(v)

# ----------------------------------
# Example 4
# Create dataset from vacancies from HeadHunter (see also Example 2 and Example 3)

# for link in vacancies[0:2]: # there's 50 vacancies on the page - let's test on some
#     link.find_element_by_css_selector("a.HH-LinkModifier").click()
#     driver.switch_to.window(driver.window_handles[0])
#     WebDriverWait(driver, 5, poll_frequency=1, ignored_exceptions=[NoSuchElementException]). \
#         until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.vacancy-serp-item")))
#
# for handle in driver.window_handles[1:]:
#     driver.switch_to.window(handle)
#     WebDriverWait(driver, 5, poll_frequency=1). \
#         until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.vacancy-description")))
#     print("---")
#     print(driver.find_element_by_css_selector("div.bloko-tag-list").text)
#     driver.close()

# list_of_links = []

# for vacancy in seq(vacancies):
#     try:
#         # list_of_links.append(vacancy.find_element_by_css_selector("a.HH-LinkModifier").get_attribute("href"))
#         pass
#         wait = WebDriverWait(driver, 5, poll_frequency=1, ignored_exceptions=[NoSuchElementException]). \
#             until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.vacancy-serp-item")))
#         vacancy.find_element_by_css_selector("a.HH-LinkModifier").get_attribute("href")
#
#     except:
#         pass

driver.quit()
