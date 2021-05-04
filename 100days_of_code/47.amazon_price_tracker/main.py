import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
USER = "spotifyhakk88@gmail.com"
PWD = "00990988"
# get data from amazon website
amazon_url = "https://www.amazon.com/Amazon-Basics-L-Shape-55-Inch-Espresso/dp/B08DWMY83P/ref=sr_1_7?dchild=1&keywords=amazonbasics&pd_rd_r=94a12bfb-4530-48b7-9503-78a3210c0fb9&pd_rd_w=LFBBF&pd_rd_wg=8B5R1&pf_rd_p=9349ffb9-3aaa-476f-8532-6a4a5c3da3e7&pf_rd_r=YS2Y10FJA3FFT9A5YYVC&qid=1620134858&sr=8-7&th=1"
header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}
response = requests.get(url=amazon_url, headers=header)
response.raise_for_status()
web_page = response.text

# using beautiful soup
target_price = 140
soup = BeautifulSoup(web_page, "lxml")
title = soup.find(id="productTitle").get_text().strip()
price = float(soup.find(name="span", id="priceblock_ourprice").getText().split("$")[1])
if price <= target_price:
    message = f"{title} is now ${price}"
    with smtplib.SMTP(host="smtp.gmail.com", port="587") as connection:
        connection.starttls()
        login = connection.login(user=USER, password=PWD)
        connection.sendmail(
            from_addr=USER,
            to_addrs=USER,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{amazon_url}"
        )
