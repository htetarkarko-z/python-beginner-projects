import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

billboard_url = "https://www.billboard.com/charts/hot-100/"

API_ID = "242b5b2ab20d4c3e9c212cbf52a556ed"
API_KEY = "325959c84acb4d1ca60aa02bcd88b93a"

# # scrape data from bill board 100 chart
# # date = input("Which year you would like to travel to in YYY-MM-DD format: ")
# date = "2000-03-18"
# response = requests.get(url=f"{billboard_url}{date}")
# web_page = response.text
# soup = BeautifulSoup(markup=web_page, features="html.parser")
# web_tags = soup.find_all(name="span", class_="chart-element__information__song")
# song_title = [web_tag.getText() for web_tag in web_tags]

#spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=API_ID,
        client_secret=API_KEY,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)