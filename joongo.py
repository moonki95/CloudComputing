from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(executable_path=r"C:\Users\mkjan\PycharmProjects\ccpp\chromedriver.exe")
url = "https://m.cafe.naver.com/ArticleSearchList.nhn?search.query=%EC%95%84%EC%9D%B4%ED%8F%B0&search.menuid=&search.searchBy=1&search.sortBy=date&search.clubid=10050146&search.option=0&search.defaultValue=1"
driver.get(url)

sleep(5)

h1 = driver.find_element_by_css_selector("#articleList > ul > li:nth-child(1) > a").click()

print(h1)

#h2 = driver.find_element_by_css_selector("#articleList > ul > li:nth-child(2) > a > div > div.tit > h3").text
#print(h2)
