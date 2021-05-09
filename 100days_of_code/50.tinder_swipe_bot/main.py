from selenium import webdriver
import time

chrome_path = "C:\Developement\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("https://tinder.com")
time.sleep(5)
driver.find_element_by_link_text("LOG IN").click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="t-531311883"]/div/div/div[1]/div/div[3]/span/div[1]/div/button').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys("arkaruchiha")