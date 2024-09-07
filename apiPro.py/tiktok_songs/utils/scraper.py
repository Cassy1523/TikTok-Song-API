import requests
from bs4 import BeautifulSoup

#web screapping 

#get tiktok page content(function)
def get_full_tiktok_song(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return None 
        
        soup = BeautifulSoup(response.text, 'html.parser')
# I created an object that has been parced, it navigates the html structure
#extracts specific elements 

#get song title 
        song_title = soup.find('a', class_='pip-0')
# The correct class will depend on the video 

#find full song
        if song_title:
            song_titles = song_title.text.strip()
            full_song = find_song_title(song_title)
        return full_song 

#errors
    except Exception as e:
        print(f"Error: {e}")
        return None 
