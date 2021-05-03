import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

billboard_url = "https://www.billboard.com/charts/hot-100/"
spotify_endpoint = "https://api.spotify.com/v1/search"

API_ID = "242b5b2ab20d4c3e9c212cbf52a556ed"
API_KEY = "325959c84acb4d1ca60aa02bcd88b93a"

# # scrape data from bill board 100 chart
date = input("Which year you would like to travel to in YYY-MM-DD format: ")
response = requests.get(url=f"{billboard_url}{date}")
web_page = response.text
soup = BeautifulSoup(markup=web_page, features="html.parser")
web_tags = soup.find_all(name="span", class_="chart-element__information__song")
song_title = [web_tag.getText() for web_tag in web_tags]

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
song_uris = []
year = date.split("-")[0]
for song in song_title:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exit in spotify. Skipped")
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
add_track = sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist["id"], tracks=song_uris)