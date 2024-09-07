from flask import Flask, request, jsonify
from utils.scraper import get_full_tiktok_song
from utils.find_music import find_song_title


# api logic and routes

app = Flask(__name__)

#Get Json data
@app.route('/find-song', methods=['POST'])
def find_song():
    data = request.json
    tiktok_url = data.get('url')
    
#check for url
    if not tiktok_url:
        return jsonify({'error': 'URL required'}), 400
    
    #Intergrate webscraping 
    song_title = get_full_tiktok_song(tiktok_url)
    

    if not song_title:
        return jsonify({'error': 'Could not retrieve song title'}), 404

#processing tiktok url
    full_song = get_full_tiktok_song(song_title)

    if full_song:
        return jsonify({'song': full_song}), 200
    else:
        return jsonify({'error': 'Song not found'}), 404 
    
def get_full_tiktok_song(url):
    # code function
    return None

if __name__ == '__main__':
    app.run(debug=False)
    
    
