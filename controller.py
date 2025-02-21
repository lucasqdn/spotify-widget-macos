import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv(dotenv_path="credentials/credentials.env")

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

sp = spotipy.Spotify(auth_manager = SpotifyOAuth(
    client_id = client_id,
    client_secret = client_secret,
    redirect_uri="http://localhost:8888/callback",
    scope = "user-read-playback-state user-modify-playback-state user-read-currently-playing"
))

def get_current_song():
    track = sp.current_playback()
    if track and track['is_playing']:
        artist = track['item']['artists'][0]['name']
        song = track['item']['name']
        return f"{song} - {artist}"
    return "None"

def next_song():
    sp.next_track();

def previous_song():
    sp.previous_track();

def pause_song():
    sp.pause_playback();

def play_song():
    sp.start_playback();