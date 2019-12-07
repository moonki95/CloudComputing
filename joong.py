from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep


# create a new chrome session
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(executable_path=r"C:\Users\mkjan\PycharmProjects\ccpp\chromedriver.exe")

driver.implicitly_wait(3)
driver.get('https://nid.naver.com/nidlogin.login')
# 아이디/비밀번호를 입력해준다.
driver.find_element_by_name('id').send_keys('mkjang0905')
driver.find_element_by_name('pw').send_keys('wkdansrl12!')
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

driver.maximize_window()
