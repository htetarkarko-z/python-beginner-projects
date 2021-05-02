from bs4 import BeautifulSoup
import requests

web_url = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url=web_url)
web_page = response.text
with open("text.txt", 'w') as file:
    file.write(web_page)

soup = BeautifulSoup(web_page, "html.praser")
web_tag = soup.find_all(name="h3")
print(web_tag)
