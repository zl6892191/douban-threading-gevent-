# from selenium import webdriver
#
# dirver = webdriver.PhantomJS()
#
# dirver.get('http://www.baidu.com')
#
# data = dirver.find_element_by_id("wrapper").text
#
# print(data)
#
# print(dirver.title)
#
# dirver.find_element_by_id('kw').send_keys('卓林')
#
# dirver.save_screenshot('baidu.png')
#
# dirver.find_element_by_id('su').click()
#
# dirver.save_screenshot('zhuolin.png')


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.baidu.com/")
data = driver.find_element_by_id("wrapper").text
print(data)

ac = driver.find_element_by_xpath("//div[@id='u1']//a[1]")
ActionChains(driver).move_to_element(ac).click(ac).perform()
