import re
from bs4 import BeautifulSoup
import requests
import constants
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# get top 100 songs
def get_billboard_top_100(user_date_input):
    url = f"https://www.billboard.com/charts/hot-100/{user_date_input}/"
    print(f"Birthday {url}")
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_="chart-results-list")
    music_list = results.find_all("h3",id="title-of-a-story", class_="a-no-trucate")
    music_title_list = []
    for music in music_list:
        music_title_list.append(music.text.strip())
    return music_title_list

# Connect with spotify and make a playlist of all the songs
def spotify_playlist(songs_title_list):
    scope = "playlist-modify-private"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=constants.client_ID, client_secret=constants.client_secret,  redirect_uri="https://example.com/", scope=scope))

    # taylor_uri = 'spotify:artist:06HL4z0CvFAxyc27GXpf02'
    # results = sp.artist_albums(taylor_uri, album_type='album')
    # albums = results['items']
    # while results['next']:
    #     results = sp.next(results)
    #     albums.extend(results['items'])

    # for album in albums:
    #     print(album['name'])


    playlist = sp.user_playlist_create(sp.current_user()['id'], "shekhars_best_of_west", public=False, collaborative=False, description='English songs')
    print(f"palylist: {playlist}")
    song_spotify_list = []
    for song in songs_title_list:
        songs = sp.search(song, limit=1, offset=0, type='track', market=None)
        print(f"song Title {song} : spotify URL {songs['tracks']['items'][0]['external_urls']['spotify']} \n\n")
        song_spotify_list.append(songs["tracks"]["items"][0]["external_urls"]["spotify"])
    sp.playlist_add_items(playlist_id=playlist["id"], items = song_spotify_list, position=None)
    



if __name__ == "__main__":

    pattern = r'[1-2]\d{3}-0\d-[0-3][0-9]|[1-2]\d{3}-1[0-2]-[0-3][0-9]'
    user_date_input = ""
    while True:
        user_date_input = input("Which Birthday you want to travel to ? Please enter the date in YYYY-MM-DD format   : ")
        if re.match(pattern, user_date_input):
            break
        else:
            print("Please enter input in correct YYYY-MM-DD format")
    songs_title_list = []
    songs_title_list = get_billboard_top_100(user_date_input)

    # call to spotify
    spotify_playlist(songs_title_list)