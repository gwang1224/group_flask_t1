import requests
import json # using .json to reorganize raw data

favorites = {}
fav_artist_list = []

def initAPI(artist): 
    """Given input of artist name, returns dictionary of api"""

    url = "https://youtube-music1.p.rapidapi.com/v2/search"
    querystring = {"query":artist}
    headers = {
	    "X-RapidAPI-Key": "4a1e45ca8dmshcde31ef8a5baed3p1a2a7ejsn9952d2cf96bd", # use personal key
	    "X-RapidAPI-Host": "youtube-music1.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    dict = json.loads(response.text)
    return dict

def album(artist):
    """input artist name, returns list of all artist's albums"""

    api_dictionary = extract_api_data(artist)
    album_list = [] # create a new list to start from scratch
    songlist = api_dictionary["result"]["songs"] # dictionary values from API dictionary

    for song in songlist:
        if song["album"]["name"] not in album_list: 
            album_list.append(song["album"]["name"])
    return album_list


def song(artist, album):
    """Given input of artist name and album 
    name, returns songs in album if query is
    found, if not, returns Information not found"""

    song_list = []
    api_dictionary = extract_api_data(artist)
    song_data = api_dictionary["result"]["songs"]

    found = False # by default nothing is found

    for song in song_data:
        if song["album"]["name"] == album: # if machine is able to find song name in dictionary then song names will be printed
            song_list.append(song["name"])
            #print(song["name"])
            found = True # variable is now set as true

    if found == False: 
        print("Information not found")
    return song_list

def fav_artist(artist):
    """Creates dictionary with artist key and number of likes in value"""
    fav_artist_list.append(artist)

    for artist in fav_artist_list:
        favorites[artist] = fav_artist_list.count(artist)
    
    return favorites

def favorites_ranked(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda x:x[1]))
    return sorted_dict

# import requests
# import

# artist = input("Enter artist name:") # allow user to input the artist they want
# #favorite_artists = [name, likes]
# #favorite_artists.append(artist)


    




# url = "https://youtube-music1.p.rapidapi.com/v2/search"

# querystring = {"query":artist}

# headers = {
# 	    "X-RapidAPI-Key": "4a1e45ca8dmshcde31ef8a5baed3p1a2a7ejsn9952d2cf96bd", # use personal key
# 	    "X-RapidAPI-Host": "youtube-music1.p.rapidapi.com"
#     }

# response = requests.request("GET", url, headers=headers, params=querystring)

# # print(response.text) # print all data that is in API


# import json # using .json to reorganize raw data

#     # define variables and assign a value
# string_val = response.text
# dict_val = json.loads(string_val)
# album_list = [] # create a new list to start from scratch
# songlist = dict_val["result"]["songs"] # dictionary values from API dictionary

# def music_function(): # define whole function
#     print("Artist's Albums:")
#     for song in songlist:
#         if song["album"]["name"] not in album_list: 
#             album_list.append(song["album"]["name"]) # if the songs album is not in the album list then the .append code will add


#     for albumname in album_list: # all albums in new album list is printed one by one
#         print(albumname)
#     album = input("Enter album name:") # let user choose an album

#     found = False # by default nothing is found
#     for song in songlist:
#         if song["album"]["name"] == album: # if machine is able to find song name in dictionary then song names will be printed
#             print("Song's in " + album)
#             print(song["name"])
#             found = True # variable is now set as true

#     if found == False: 
#         print("Information not found") # if correct info not added then output will tell user

# music_function() # call the function that was defined before