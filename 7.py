from time import sleep
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_driver_path = 'C:\chromedriver.exe'
driver = webdriver.Chrome(chrome_driver_path )

driver.get('https://nid.naver.com/nidlogin.login')
# 아이디/비밀번호를 입력해준다.
#driver.find_element_by_name('id').send_keys('id')
#driver.find_element_by_name('pw').send_keys('pw')
id='wjdalsrbekt'
pw='alsrb123!'
#
dt=datetime.datetime.now()
filename=dt.strftime("%Y_%m_%d")
f=open(filename+'.csv','w')
#
driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")

driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

sleep(3)
url = "https://m.cafe.naver.com/ArticleSearchList.nhn?search.query=%EC%95%84%EC%9D%B4%ED%8F%B0&search.menuid=&search.searchBy=0&search.sortBy=date&search.clubid=10050146&search.option=0&search.defaultValue=1"
driver.get(url)
sleep(3)

#d1 = driver.find_element_by_css_selector("#moreButtonArea > div").click()
#d1 = driver.find_element_by_css_selector("#moreButtonArea > div").click()
for j in range (1,2):
    for i in range(1,5):
        sleep(3)
        #prodcut_link : 상품 url
        product_link = driver.find_element_by_css_selector("#articleList > ul:nth-child(%d) > li:nth-child(%d) > a"%(j,i)).get_attribute('href')
        sleep(2)
        #product_name : 상품 이름
        product_name = driver.find_element_by_css_selector("#articleList > ul:nth-child(%d) > li:nth-child(%d) > a > div > div.tit > h3" % (j,i)).text
        #product_page : 상품 페이지로 가기
        product_page = driver.find_element_by_css_selector("#articleList > ul:nth-child(%d) > li:nth-child(%d) > a"%(j,i)).click()
        sleep(3)
        try :
            driver.find_element_by_class_name('tran_type')
            product_price = driver.find_element_by_class_name('price').text
            #
            product_price2 = product_price.replace("원", "")
            arr=product_price2.split(',')
            #print(arr)
            joined_arr="".join(arr)
            print(joined_arr)
            f.write(joined_arr+ '\n')
            print(product_price)
        except :
            i=i+1
            driver.back()
            continue
        driver.back()
    #product_more : 더보기 기능
    product_more = driver.find_element_by_css_selector("#moreButtonArea > div").click()

f.close()
sleep(3)