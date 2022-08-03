import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# options.add_argument('--headless') # Background process

driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://leetcode.com/accounts/login/?next=/problemset/all/'
driver.get(url)
time.sleep(3) #wait for page open
driver.find_element_by_id('id_login').send_keys('Gkotta') #user name
driver.find_element_by_id('id_password').send_keys('*****') #password
driver.find_element_by_id('signin_btn').click() #signin
time.sleep(5) #wait for page open
xpath = '//*[@id="__next"]/div/div/div[1]/div[1]/div[6]/div[2]/div/div/div[2]/div[1]/div[1]'#dayly problem
print(driver.find_element_by_xpath(xpath).get_attribute('href'))

out = input('press 1 to out')
driver.quit()
