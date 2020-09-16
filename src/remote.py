from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from functional import seq
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
driver.get("https://github.com/mezlogo/there_is_a_huge_snake_inside_my_jeans")
#get list of all files in repository
#you can test this query by javascript console in browser `document.querySelectorAll("div.Details div.Box-row")`
arrayOfWebElements = driver.find_elements_by_css_selector("div.Details div.Box-row")
#convert to PyFunctional seq https://github.com/EntilZha/PyFunctional
elems = seq(arrayOfWebElements)
#print pairs of file name and file type (dir of plain file)
#example for js with only file name
#document.querySelectorAll("div.Details div.Box-row")[0].querySelector("a[title]").getAttribute("title")
#example with pair of type and title
#Array.from(document.querySelectorAll("div.Details div.Box-row")).map(elem => "title: " + elem.querySelector("svg[aria-label]").getAttribute("aria-label") + " type: " + elem.querySelector("a[title]").getAttribute("title"))
print(elems.map(lambda elem:
    "type: " +
    elem.find_element_by_css_selector("svg[aria-label]").get_attribute("aria-label")
    + " titile: " + 
    elem.find_element_by_css_selector("a[title]").get_attribute("title"))
)
driver.quit()