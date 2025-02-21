import rumps
from controller import get_current_song, play_song, pause_song, next_song, previous_song
class spotifyWidgetApp(rumps.App):
    def __init__(self):
        super(spotifyWidgetApp, self).__init__("Spotify Controller")
        self.update_title()
    
    def update_title(self, _=None):
        song_name = get_current_song()
        self.title = song_name
        rumps.Timer(self.update_title, 1).start()

    @rumps.clicked("Play/Pause")
    def play_pause(self, _):
        if get_current_song() == "None":
            play_song()
        else:
            pause_song()
    
    @rumps.clicked("Next")
    def next_song(self, _):
        next_song()

    @rumps.clicked("Previous")
    def previous_song(self, _):
        previous_song()