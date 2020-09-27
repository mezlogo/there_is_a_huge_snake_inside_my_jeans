from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from functional import seq
from selenium.common.exceptions import *
from globals import chromedriver

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
driver.get("https://spb.hh.ru/vacancies/data-scientist")
vacancies = driver.find_elements_by_css_selector("div.vacancy-serp-item")
list_of_vacancies = []

for vacancy in seq(vacancies):
    try:
        list_of_vacancies.append(vacancy.find_element_by_css_selector("a.HH-LinkModifier").get_attribute("text"))
        list_of_vacancies.append(vacancy.find_element_by_css_selector("a[data-qa=\"vacancy-serp__vacancy-employer\"]").get_attribute("text"))
        list_of_vacancies.append(vacancy.find_element_by_css_selector("span[data-qa=\"vacancy-serp__vacancy-compensation\"]").text)

    except NoSuchElementException:
        list_of_vacancies.append(None)

separated_vacancies = [list_of_vacancies[x:x+3] for x in range(0, len(list_of_vacancies), 3)]
print(*separated_vacancies)

# list_of_vacancies = seq(vacancies).map(lambda vacancy:
#     [vacancy.find_element_by_css_selector("a.HH-LinkModifier").get_attribute("text"),
#      vacancy.find_element_by_css_selector("a[data-qa=\"vacancy-serp__vacancy-employer\"]").get_attribute("text")])
# print(list_of_vacancies)

# print(*seq(vacancies).map(lambda vacancy:
#     [vacancy.find_element_by_css_selector("a.HH-LinkModifier").get_attribute("text"),
#      vacancy.find_element_by_css_selector("a[data-qa=\"vacancy-serp__vacancy-employer\"]").get_attribute("text")])
# )

driver.quit()