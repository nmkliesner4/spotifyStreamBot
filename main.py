import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
from time import sleep
from random import randrange

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=scope, redirect_uri=REDIRECT_URI, client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

sp.volume(1)
while True:
    sp.start_playback(uris=["spotify:track:7eSSmgq26BXr7xay3WKjfi"])
    rand = randrange(31,36)
    sleep(rand)