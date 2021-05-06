from selenium import webdriver
import time
chrome_driver = r"C:\Developement\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

#Get cookie to click on.
cookie = driver.find_element_by_id("cookie")

# get upgrade item ids
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

time_out = time.time() + 5
five_min = time.time() + 60 * 5  # 5 mins

while True:
    cookie.click()

    #Every 5 secs
    if time.time() > time_out:
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_prices = [
            price.text.split("-")[1].strip().replace(",", "")
            for price in all_prices if price.text != ""]
        cookie_upgrade = {}
        for n in range(len(item_prices)):
            cookie_upgrade[item_prices[n]] = item_ids[n]

        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        affordable_upgrades = {
            cost: id for cost, id in cookie_upgrade.items()
            if cookie_count > int(cost)}

        #highest price
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
        driver.find_element_by_id(to_purchase_id).click()
        time_out = time.time() + 5
    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break
