from selenium import webdriver

driver = webdriver.Chrome('/Users/beomi/Downloads/chromedriver')
driver.implicitly_wait(3)
driver.get('https://nid.naver.com/nidlogin.login')
driver.find_element_by_name('id').send_keys('')
driver.find_element_by_name('pw').send_keys('')
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()