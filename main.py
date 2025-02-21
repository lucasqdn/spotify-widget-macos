import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

sp = spotipy.Spotify(auth_manager = SpotifyOAuth(
    client_id = client_id,
    client_secret = client_secret,
    redirect_uri="http://localhost:8888/callback",
    scope="user-read-currently-playing user-modify-playback-state"
))
