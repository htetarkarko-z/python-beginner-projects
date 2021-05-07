from selenium import webdriver
import time

USER = "spotifyhakk88@gmail.com"
PWD = "asUEkyCMgULx25A"

chrome_path = r"C:\Developement\chromedriver.exe"
linkedin_url = "https://www.linkedin.com/jobs/search/?keywords=python%20developer"
driver = webdriver.Chrome(executable_path=chrome_path)
driver.get(linkedin_url)
driver.find_element_by_link_text("Sign in").click()

time.sleep(1)
email = driver.find_element_by_id("username")
email.send_keys(USER)
password = driver.find_element_by_id("password")
password.send_keys(PWD)
driver.find_element_by_css_selector(".login__form_action_container button").click()