import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials 


#authenticate the api 
sp = spotipy.Spotify(manage_auth=SpotifyClientCredentials)(
    client_id = "67bb500f7f2c4744a187046d974b6672",
    client_secret= "5c4c86aa44c940eea53993c281614c41"
)

# find song using title 
def find_song_title(song_title):
    results = sp.search(q=song_title, type='track', limit=1)
    if results['tracks']['items']:
        track = results['track']['items'][0]
        song_name = track['name']
        singer_name = track['artist'][0]['name']
        return(f"{song_name} by {singer_name}") 
    return None 