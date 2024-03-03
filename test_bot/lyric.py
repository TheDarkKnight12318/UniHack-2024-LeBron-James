import json
import requests

singer = 'Taylor Swift'
song_name = 'Delicate'

class lyric_getter:

    def get_lyrics(artist, song_title):
        #Fetch lyrics
        try:
            url = 'https://api.lyrics.ovh/v1/' + artist + '/' + song_title
            response = requests.get(url)
            json_data = json.loads(response.content)
            lyrics = json_data['lyrics']
            return lyrics
        except:
            #Prints if previous statement comes out as error
            return_message = 'Could not find song or artist'
            return return_message
lyrics = lyric_getter.get_lyrics(singer, song_name)
#for lyrics == '\n':
    #print(lyrics[0])

# print(lyric_getter.get_lyrics(singer, song_name))
# print(type(lyric_getter.get_lyrics(singer, song_name)))