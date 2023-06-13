import requests, os
from dotenv import load_dotenv

load_dotenv('.env')

# Client Keys
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

# base URL of all Spotify API endpoints
BASE_URL = 'https://api.spotify.com/v1/'

playlist1_id = 'spotify:playlist:4SvH0DVPmWoWDJRk0gZZ6A'.split(':')[2]

playlist1 = requests.get(BASE_URL + 'playlists/' + playlist1_id, headers=headers)
playlist1 = playlist1.json()


playlist2_id = 'spotify:playlist:61lKq857UUy2jpka28RCr7'.split(':')[2]

playlist2 = requests.get(BASE_URL + 'playlists/' + playlist2_id, headers=headers)
playlist2 = playlist2.json()


songs = playlist2['tracks']['items']
songs = [song['track']['name'] for song in songs if song['track']['id'] is not None]


same_tracks = []
for track in playlist1['tracks']['items']:
    track = track['track']
    
    if track['name'] in songs:
        same_tracks.append(track['uri'])


data = {
    'tracks': [
        {
            'uri': 'spotify:track:0jA4h2SD50Oak4C3Vn905a',
            'uri': 'spotify:track:3pANfZVFdtuVnJsE6xa5Ox',
        }
    ]
}

remove = requests.delete(BASE_URL + 'playlists/' + playlist1_id + '/tracks', headers=headers, json=data)
print(remove.json())