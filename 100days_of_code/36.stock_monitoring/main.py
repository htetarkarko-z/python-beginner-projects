import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

NEWS_API = "e86abdb771a443fea9fcebc02533ab20"
STOCK_API = "K3BOI25PTMKQ0SRO"
TWILIO_SID = "AC666b2f85d93b340d8903d2951a8c9979"
TWILIO_AUTH = "e8dd0887db370ece86bdd1cf69211d7e"

STOCK_API = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_param = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API,
}
news_param = {
    "apiKey": NEWS_API,
    "qInTitle": COMPANY_NAME,
}

response = requests.get(url=STOCK_API, params=stock_param)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]
stock_list = [value for (key, value) in stock_data.items()]
yesterday_data = stock_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])
day_before_yesterday_data = stock_list[1]
day_before_yesterday_closing_price = float(
    day_before_yesterday_data["4. close"])
difference = yesterday_closing_price - day_before_yesterday_closing_price
up_down = None
if difference > 0:
    up_down = "🔼"
else:
    up_down = "🔽"

diff_pecent = (difference / yesterday_closing_price) * 100


if abs(diff_pecent) > 0:
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_param)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    three_atricles = articles[:3]
    formatted_article = [
        f"{COMPANY_NAME}: {up_down}{diff_pecent}%\nHeadline: {article['title']}. \nBreif: {article['description']}" for article in three_atricles]

    client = Client(TWILIO_SID, TWILIO_AUTH)

    for article in formatted_article:
        print(article)
        message = client.messages.create(
            body=article,
            from_="+17603875087",
            to="+95 9 44971 3063",
        )
    print(message.status)
