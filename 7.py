from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_driver_path = 'C:\chromedriver.exe'
driver = webdriver.Chrome(chrome_driver_path )

driver.get('https://nid.naver.com/nidlogin.login')
# 아이디/비밀번호를 입력해준다.
#driver.find_element_by_name('id').send_keys('id')
#driver.find_element_by_name('pw').send_keys('pw')
id='ID'
pw='password'
driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")

driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

sleep(3)
url = "https://m.cafe.naver.com/ArticleSearchList.nhn?search.query=%EC%95%84%EC%9D%B4%ED%8F%B0&search.menuid=&search.searchBy=1&search.sortBy=date&search.clubid=10050146&search.option=0&search.defaultValue=1"
driver.get(url)
sleep(3)

#d1 = driver.find_element_by_css_selector("#moreButtonArea > div").click()
d1 = driver.find_element_by_css_selector("#moreButtonArea > div").click()
for j in range (1,40):
    for i in range(1,20):
        sleep(3)
        h3 = driver.find_element_by_css_selector("#articleList > ul:nth-child(%d) > li:nth-child(%d) > a"%(j,i)).get_attribute('href')
        sleep(2)
        h2 = driver.find_element_by_css_selector("#articleList > ul:nth-child(%d) > li:nth-child(%d) > a > div > div.tit > h3"%(j,i)).text
        h1 = driver.find_element_by_css_selector("#articleList > ul:nth-child(%d) > li:nth-child(%d) > a"%(j,i)).click()
        sleep(3)
        try :
            driver.find_element_by_class_name('tran_type')
            selected_class = driver.find_element_by_class_name('price').text
            print(h3)
            print(h2)
            print(selected_class)
            print("현재 숫자 : %d %d"%(j,i))
        except :
            i=i+1
            driver.back()
            continue
        driver.back()
    d1 = driver.find_element_by_css_selector("#moreButtonArea > div").click()

sleep(3)