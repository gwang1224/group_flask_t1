import requests
import json # using .json to reorganize raw data

favorites = {}
fav_artist_list = []
ts_albums = ["Taylor Swift", "Fearless", "Speak Now", "Red", "1989", "Reputation", 
            "Lover", "Folklore", "Evermore", "Midnights"]
fav_albums = {}

# setup ts_albums
for album in ts_albums:
    fav_albums[album] = {"likes": 0}

def initAPI(): 
    """Given input of artist name, returns dictionary of api"""

    url = "https://youtube-music1.p.rapidapi.com/v2/search"
    querystring = {"query":"Taylor Swift"}
    headers = {
	    "X-RapidAPI-Key": "4a1e45ca8dmshcde31ef8a5baed3p1a2a7ejsn9952d2cf96bd", # use personal key
	    "X-RapidAPI-Host": "youtube-music1.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    dict = json.loads(response.text)
    return dict


def album():
    """input artist name, returns list of all artist's albums"""

    api_dictionary = initAPI()
    album_list = [] # create a new list to start from scratch
    songlist = api_dictionary["result"]["songs"] # dictionary values from API dictionary

    for song in songlist:
        if song["album"]["name"] not in album_list: 
            album_list.append(song["album"]["name"])
    return album_list

def song(album):
    """Given input of artist name and album 
    name, returns songs in album if query is
    found, if not, returns Information not found"""

    song_list = []
    api_dictionary = initAPI()
    song_data = api_dictionary["result"]["songs"]

    found = False # by default nothing is found

    for song in song_data:
        if song["album"]["name"] == album: # if machine is able to find song name in dictionary then song names will be printed
            song_list.append(song["name"])
            #print(song["name"])
            found = True # variable is now set as true
    return song_list

def fav_artist(artist):
    """Creates dictionary with artist key and number of likes in value"""
    fav_artist_list.append(artist)

    for artist in fav_artist_list:
        favorites[artist] = fav_artist_list.count(artist)
    
    sorted_dict = dict(sorted(favorites.items(), key=lambda x:x[1]))
    res = dict(reversed(list(sorted_dict.items())))

    return res

def add_like(album):
    fav_albums[album]["likes"] = fav_albums[album]["likes"] + 1
    return fav_albums[album]["likes"]

def getLikes():
    return fav_albums

def getAlbum(album):
    return fav_albums[album]



album_list = ['Midnights', 'Midnights (3am Edition)', 'reputation', 'This Love (Taylorâ€™s Version)', "Fearless (Taylor's Version)", '1989', 'Bad Blood', 'Speak Now', 'Lover', "Red (Taylor's Version)", '1989 (Deluxe Edition)', 'Red', 'Today Was A Fairytale']
as_dict = {}
def add_element(dict, key, value):
    if key not in dict:
        dict[key] = []
    dict[key].append(value)
def album_song():
    for i in range(len(album_list)):
        album_var = album_list[i]
        # print(album_var)
        song1 = song(album_var)
        #songs = song(album_var)
        #as_dict[album_var].append(songs)
        add_element(as_dict, album_var, song1)
    return as_dict
    print(as_dict)
album_song()
